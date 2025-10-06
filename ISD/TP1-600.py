from sklearn import neighbors as nn
from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics


#Chargement des données
digitsData = load_digits()
X = digitsData.data
y = digitsData.target

#Créer un classifieur KNN avec k=3 et distance minkosky = 2
clf = nn.KNeighborsClassifier(n_neighbors=3,p=2)

clf.fit(X, y)

#Faire prédictions
y_pred = clf.predict(X)

matrix = metrics.confusion_matrix(y,y_pred)

confusion_matrix_Display = metrics.ConfusionMatrixDisplay(matrix)

confusion_matrix_Display.plot()
plt.show()


