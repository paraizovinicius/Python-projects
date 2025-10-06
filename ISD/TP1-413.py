from sklearn.model_selection import train_test_split
from sklearn import neighbors as nn
from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt

digitsData = load_digits()
X = digitsData.data
y = digitsData.target


errors = []
for i in range(10):

    # production de deux sous-échantillon
    Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,test_size=0.3, random_state=None) 

    clf = nn.KNeighborsClassifier(3)
    clf.fit(Xtrain, ytrain)
    error = 1 - clf.score(Xtrain, ytrain)  # Calcul de l'erreur d'apprentissage (1 - )
    errors.append(error)
    
avg_error = np.mean(errors)

print(f"Estimation de l'erreur réelle (moyenne sur 10 séquences) : {avg_error}")
