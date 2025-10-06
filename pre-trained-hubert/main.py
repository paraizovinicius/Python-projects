import multiprocessing
import os
import joblib
import librosa
import numpy as np
from sklearn.cluster import MiniBatchKMeans
import torch
import torchaudio
from transformers import AutoProcessor, HubertModel

# List all files directly in the folder (ignoring ".")
dir = '/baie/nfs-cluster-1/data1/raid1/homedirs/vinicius.paraizo'
mp3_folder = f'{dir}\mp3_files' # Folder with the mp3 files TESTE
mp3_files = [f for f in os.listdir(mp3_folder)]

# Addind the full path to each element in array
mp3_files = [mp3_folder + '/' + f for f in mp3_files]

# Specify the desired target sample rate
target_sr = 16000

# Segment duration in seconds
segment_duration = 30

# Array to define list of musics and number of segments
music_segment_info = []

def segment_audio(audio, i):
    
    num_segments = int(audio.shape[0] / (target_sr * segment_duration)) # Calculate number of segments
    print(f"\nAudio {i}. Number of segments: {num_segments}\n")
    
    music_segment_info.append((i, num_segments))

    for segment_index in range(num_segments):
      start_index = segment_index * target_sr * segment_duration
      end_index = start_index + target_sr * segment_duration

      segment_audio = audio[start_index:end_index]
      
      # Convert it to a 2D array so we can convert it to a torch tensor
      segment_audio = segment_audio.reshape(1, -1)
      
      # Convert numpy array to torch tensor (if needed)
      segment_tensor = torch.from_numpy(segment_audio).float()

      # Save the segment into a file
      segment_file = f"{i}_{segment_index}.mp3"
      
      segment_file = os.path.join(mp3_folder, segment_file)  # Add the mp3_folder path to the segment_file
      torchaudio.save(segment_file, segment_tensor, sample_rate=16000)  # Save the segment into the mp3_folder
        
        

all_segments = []
# Load the audio file
for i, file in enumerate(mp3_files):
    audio, sample_rate = librosa.load(file, sr=target_sr)
    segment_audio(audio, i)


# Now that we have the segments, we can use the Hubert model to extract the hidden states

processor = AutoProcessor.from_pretrained("facebook/hubert-large-ls960-ft")
model = HubertModel.from_pretrained("facebook/hubert-large-ls960-ft")

# The processor handles tokenization and feature extraction

concatenated_hidden_states = []
shards = []
for music_info in music_segment_info:
  music_index = music_info[0]
  segments_number = music_info[1]
  
  for i in range(segments_number):
    print(f"Computing hidden states for segment {i} of music {music_index}\n")
    segment = f"{mp3_folder}\{music_index}_{i}.mp3"
    audio, _ = librosa.load(segment, sr=target_sr)# Load the audio segment
    input_values = processor(audio, sampling_rate=target_sr, return_tensors="pt").input_values
    hidden_states = model(input_values).last_hidden_state
    concatenated_hidden_states.append(hidden_states) # Concatenating every segment into one variable
   
    concatenated_hidden_states = torch.cat(concatenated_hidden_states, dim=0) # Concatenate the hidden states tensors along dimension 1 (segments)

    concatenated_hidden_states = concatenated_hidden_states.view(-1, hidden_states.shape[-1])# Reshape the concatenated tensor to 2D
    
  shards.append(concatenated_hidden_states) # append the concatenated segments into shards. Every element in the shards list represents a music
  
# Print the shapes of the tensors
print("Shape of concatenated hidden states tensor:", concatenated_hidden_states.shape)
print("Shape of 1st shard: ", shards[0].shape)


# To fit a k-means model with 500 clusters on the data

def fit_kmeans(shard, dir, i):
  # Applying Kmeans to all data. No percentage is applied
  km_model = MiniBatchKMeans(
      n_clusters=500,
      init="k-means++",
      max_iter=100,
      batch_size=10000, # default 1024
      tol=0.0,
      max_no_improvement=100,
      n_init=20,
      reassignment_ratio=0.0,
  )
  km_model.fit(shard)
    
  km_path = f"{dir}\kmeans\kmeans_{i}.joblib"
  joblib.dump(km_model, km_path) # This file allows you to save the trained model to disk
    
  inertia = -km_model.score(shard) / len(shard)
  print("\n", inertia)

#num_processes = 1 # Use all available CPU cores
#pool = multiprocessing.Pool(processes=num_processes)



# Assuming shards is your list of data tensors
for i in range(len(shards)):
  print(f"Computing Kmeans for shard {i}")
  shard = shards[i].detach().numpy()
  #pool.apply_async(fit_kmeans, args=(shard, dir, i))
  fit_kmeans(shard, dir, i)
    
#pool.close()
#pool.join()
