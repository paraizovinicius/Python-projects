from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score, silhouette_score, adjusted_rand_score
import numpy as np

# Load the dataset
df = pd.read_csv("C:\\Users\\parai\\Downloads\\unpopular_songs_full.csv")
df = df.drop(['Unnamed: 17', 'track_id', 'track_name', 'track_artist', 'explicit'], axis=1)

X = df.drop(['popularity'], axis=1)
y = df['popularity']

# Check distribution of 'popularity'
print("Popularity distribution:", y.value_counts())

for i in range(10):

    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.3, stratify=y) # split 30% test sur le jeu de données
    kmeans = KMeans(n_clusters=2, n_init=10)    #  KMeans clustering avec le nombre de clusters optimal = 2
    kmeans.fit(Xtrain)


    if len(set(kmeans.labels_)) == 1:  # Check if labels are assigned to only one cluster
        print("")
        continue

    y_test_pred = kmeans.predict(Xtest)#  Déterminer, pour chaque élément du jeu test, le cluster auquel il appartient

    # 4 Calculer les metrics on the training set:
    # a) Davies Bouldin score
    db_score = davies_bouldin_score(Xtrain, kmeans.labels_)
    print(f"Davies Bouldin Score sur le jeu d'apprentissage: {db_score}")

    # b) Silhouette score
    silhouette_avg = silhouette_score(Xtrain, kmeans.labels_)
    print(f"Average Silhouette Score sur le jeu d'apprentissage: {silhouette_avg}")

    # 5. Calculate metrics on the test set:
    # a) Davies Bouldin score
    db_score_test = davies_bouldin_score(Xtest, y_test_pred)
    print(f"Davies Bouldin Score sur le jeu test: {db_score_test}")

    # b) Silhouette score
    silhouette_avg_test = silhouette_score(Xtest, y_test_pred)
    print(f"Average Silhouette Score sur le jeu test: {silhouette_avg_test}")

    # Rand Index
    rand_index_train = adjusted_rand_score(ytrain, kmeans.labels_)# le jeu d'apprentissage
    print(f"Rand Index sur le jeu d'apprentissage: {rand_index_train}")

    rand_index_test = adjusted_rand_score(ytest, y_test_pred) # le jeu test
    print(f"Rand Index sur le jeu test: {rand_index_test}")