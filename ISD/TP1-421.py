
from sklearn import neighbors as nn
from sklearn.datasets import load_digits
import numpy as np
from sklearn.model_selection import cross_val_score

#Chargement des données
digitsData = load_digits()
X = digitsData.data
y = digitsData.target

#Créer un classifieur KNN avec k=3
clf = nn.KNeighborsClassifier(n_neighbors=3)

#Effectuer une validation croisée avec cv = 5
scores = cross_val_score(clf, X, y, cv=5, scoring='f1_weighted')

#l'estimation de l'erreur
average_error = 1 - np.mean(scores)

print(f"Estimation de l'erreur réelle par validation croisée : {average_error}")


