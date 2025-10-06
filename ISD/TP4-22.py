from matplotlib import pyplot as plt
import pandas as pd
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

df = pd.read_csv("C:\\Users\\parai\\Downloads\\unpopular_songs_full.csv")# Load archive unpopular songs
X = df

X = df.drop(['Unnamed: 17', 'track_id', 'track_name', 'track_artist', 'popularity', 'key', 'explicit'], axis=1)# Supprimer ls collones non-descritives

# Calculer le score de silhouette pour les différents nombres de clusters
silhouette_scores = []
RangeClusters = [2, 3, 4, 5, 6, 7, 8]

for num_clusters in RangeClusters:
    gmm = GaussianMixture(n_components=num_clusters) 
    gmm.fit(X)
    labels = gmm.predict(X)
    silhouette_score_value = silhouette_score(X, labels)
    silhouette_scores.append(silhouette_score_value)
OptimalNumClusters = RangeClusters[silhouette_scores.index(max(silhouette_scores))]# Sélectionner le nombre de clusters optimal

# Évaluer la qualité du clustering obtenu avec la popularité des chansons
X1 = df
X1 = df.drop(['Unnamed: 17', 'track_id', 'track_name', 'track_artist', 'explicit'], axis=1)
gmm = GaussianMixture(n_components=OptimalNumClusters)
gmm.fit(X1)
labels = gmm.predict(X1)
print(f"L'évaluation de la qualité avec la popularité des chansons: {silhouette_score(X1, labels)}" )

# Évaluer la qualité du clustering obtenu sans la popularité des chansons
X2 = df
X2 = df.drop(['Unnamed: 17', 'track_id', 'track_name', 'track_artist', 'popularity', 'key', 'explicit'], axis=1)
gmm = GaussianMixture(n_components=OptimalNumClusters)
gmm.fit(X2)
labels = gmm.predict(X2)
print(f"Sans la popularité des chansons:{silhouette_score(X2, labels)} ")


