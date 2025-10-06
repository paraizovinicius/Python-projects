from sklearn.model_selection import train_test_split
from sklearn import neighbors as nn
from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt

digitsData = load_digits()
X = digitsData.data
print(len(X))
print(X.shape)


y = digitsData.target

# production de deux sous-échantillon
Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,test_size=0.3, random_state=42) 

k_values = np.arange(1, 36)
errors = []
for k in k_values:
    clf = nn.KNeighborsClassifier(k)
    clf.fit(Xtrain, ytrain)
    error = 1 - clf.score(Xtrain, ytrain)  # Calcul de l'erreur d'apprentissage (1 - )
    errors.append(error)
    
real_error = 1 - clf.score(Xtest, ytest)
print(real_error)

plt.plot(k_values, errors)
plt.xlabel('Valeurs de k')
plt.ylabel('Erreur d\'apprentissage')
plt.title('Évolution de l\'erreur d\'apprentissage en fonction de k')
plt.show()


