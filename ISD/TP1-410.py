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
print(Xtrain[:3,:], ytrain[:3])
print(Xtest[:3,:], ytest[:3])

print()

Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,test_size=0.25, random_state=32) 
print(Xtrain[:3,:], ytrain[:3])
print(Xtest[:3,:], ytest[:3])