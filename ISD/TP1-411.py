from sklearn.model_selection import train_test_split
from sklearn import neighbors as nn
from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt

digitsData = load_digits()
X = digitsData.data
y = digitsData.target
 



# production de deux sous-échantillon
Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,test_size=0.25, random_state=42) 


clf = nn.KNeighborsClassifier(n_neighbors=3)
clf.fit(Xtrain, ytrain)

# Test le classifieur sur le second sous-échantillon
précision = clf.score(Xtest, ytest)

print(f"Précision: {1-précision}")

