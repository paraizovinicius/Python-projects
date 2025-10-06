from matplotlib import pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import rand_score
from sklearn.metrics import silhouette_score

# Abre o arquivo unpopspotify.csv
df = pd.read_csv("C:\\Users\\parai\\Downloads\\unpopular_songs_full.csv")

# Supprimer ls collones non-descritives
X = df.drop(['Unnamed: 17', 'track_id', 'track_name', 'track_artist', 'explicit'], axis=1)

# Apprendre un regroupement k-means
kmeans = KMeans(n_clusters=2, n_init=10)
kmeans.fit(X)
labels_kmeans = kmeans.labels_

# Apprendre un regroupement mélange de gaussiennes
gmm = GaussianMixture(n_components=2)
gmm.fit(X)
labels_gmm = gmm.predict(X)


rand_index = rand_score(labels_kmeans, labels_gmm)# Faire le rand index entre eux

print(f"Le rand index entre les deux methodes: {rand_index}")
print()

# Calculer le score de silhouette parmi ces 2 methodes

silhouette_score_kmeans = silhouette_score(X, labels_kmeans)# KMeans clustering
silhouette_score_gmm = silhouette_score(X, labels_gmm)# Gaussian Mixture Model clustering

print(f"Silhouette score pour KMeans clustering: {silhouette_score_kmeans}")
print(f"Silhouette score pour Gaussian Mixture Model clustering: {silhouette_score_gmm}")

print()
# Calculer le nombre d'exemples de popularité 3 dans chaque cluster
cluster_popularity_3 = [0] * 2
for i in range(len(labels_gmm)):
  if df.loc[i, "popularity"] == 3:
    cluster_popularity_3[labels_gmm[i]] += 1

# Imprimer le nombre d'exemples de popularité 3 dans chaque cluster
print("Nombre d'exemples de popularité 3 dans chaque cluster :")
for i in range(len(cluster_popularity_3)):
  print(f"Cluster {i} : {cluster_popularity_3[i]}")
  
print()
# Calculer le nombre d'exemples de popularité 2 dans chaque cluster
cluster_popularity_2 = [0] * 2
for i in range(len(labels_gmm)):
  if df.loc[i, "popularity"] == 2:
    cluster_popularity_2[labels_gmm[i]] += 1

# Imprimer le nombre d'exemples de popularité 2 dans chaque cluster
print("Nombre d'exemples de popularité 2 dans chaque cluster :")
for i in range(len(cluster_popularity_2)):
  print(f"Cluster {i} : {cluster_popularity_2[i]}")
  
  
print()
# Calculer le rand index
rand_index_gmm = rand_score(df["popularity"], labels_gmm)

# Imprimer le rand index
print(f"Rand index du clustering GMM : {rand_index_gmm}")


# indiquer les chansons les plus proches de chacun des centres des clusters.

print()

