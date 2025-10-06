from sklearn import neighbors as nn
from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt

digitsData = load_digits()
X = digitsData.data
y = digitsData.target

# Initialisation des listes pour stocker les valeurs de k et les erreurs
k_values = np.arange(1, 36)
errors = []

for k in k_values:
    clf = nn.KNeighborsClassifier(k)
    clf.fit(X, y)
    error = 1 - clf.score(X, y)  # Calcul de l'erreur d'apprentissage (1 - )
    errors.append(error)

# Affichage de la courbe
plt.plot(k_values, errors)
plt.xlabel('Valeurs de k')
plt.ylabel('Erreur d\'apprentissage')
plt.title('Évolution de l\'erreur d\'apprentissage en fonction de k')
plt.show()