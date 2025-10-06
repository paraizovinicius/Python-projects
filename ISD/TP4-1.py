from matplotlib import pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Abre o arquivo unpopspotify.csv
df = pd.read_csv("C:\\Users\\parai\\Downloads\\unpopular_songs_full.csv")
X = df
# Supprimer ls collones non-descritives (sur tous les données)
X = df.drop(['Unnamed: 17', 'track_id', 'track_name', 'track_artist', 'popularity', 'key', 'explicit'], axis=1)
for column in X:
    print(column)
print()


# Deuxième question au-dessus

silhouette_avg = []
rangeClusters = [2, 3, 4, 5, 6, 7, 8]

for numClusters in rangeClusters:  # Calculez l'indice de silhouette avec différents nombres de clusters
    kmeans = KMeans(n_clusters=numClusters, n_init=10)
    kmeans.fit(X)
    labels = kmeans.labels_
    silhouette_avg.append(silhouette_score(X, labels))# l'indice de silhouette pour découvrir le NumCluster avec la qualité la plus grand
        
optimal_num_clusters = rangeClusters[silhouette_avg.index(max(silhouette_avg))]# Sélectionner le nombre de clusters optimal
plt.plot(rangeClusters,silhouette_avg,"bx-")
plt.xlabel("Values of K") #plt.ylabel("Silhouette score") 
plt.title("Silhouette analysis For Optimal k")

print(f"silhouette_avg={silhouette_avg}")
print(f"silhouette_optimum={optimal_num_clusters}")
plt.show() 


print(f"silhouette_avg={silhouette_avg}")
print(f"silhouette_optimum={optimal_num_clusters}")


# Troisième Question au-dessous


print()
# Évaluer la qualité du clustering obtenu avec la popularité des chansons
X1 = df
X1 = df.drop(['Unnamed: 17', 'track_id', 'track_name', 'track_artist', 'explicit'], axis=1)
kmeans = KMeans(n_clusters=optimal_num_clusters, n_init=10)
kmeans.fit(X1)
labels = kmeans.labels_
print(f"Avec la popularité des chansons: {silhouette_score(X1, labels)}")

print()


# Évaluer la qualité du clustering obtenu sans la popularité des chansons
X2 = df
X2 = df.drop(['Unnamed: 17', 'track_id', 'track_name', 'track_artist', 'popularity', 'explicit'], axis=1)
kmeans = KMeans(n_clusters=optimal_num_clusters, n_init=10)
kmeans.fit(X2)
labels = kmeans.labels_
print(f"Sans la popularité des chansons: {silhouette_score(X2, labels)}")
