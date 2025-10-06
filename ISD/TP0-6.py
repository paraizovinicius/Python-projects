import numpy as np
from sklearn.datasets import load_digits
import random
import math


digits = load_digits()
miss_digits = load_digits()
nbmissingvalues = random.randint(1000,2000)
for imissingvalue in range(nbmissingvalues):
    lig = random.randint(0,1763)
    col = random.randint(0,63)
    miss_digits.data[lig,col] = math.nan

mdd1 = miss_digits.data.copy() # pour tester methode 1
mdd2 = miss_digits.data.copy() # pour tester methode 2
mdd3 = miss_digits.data.copy() # pour tester methode 3


def count_missing_values(data):
  return np.count_nonzero(np.isnan(data))

def count_missing_values_by_column(data):
  return np.sum(np.isnan(data), axis=0)

nb_missing_values_global = count_missing_values(miss_digits.data)

nb_missing_values_by_column = count_missing_values_by_column(miss_digits.data)

print("Nombre de valeurs manquantes globalement :", nb_missing_values_global)
print("Nombre de valeurs manquantes par colonne :", nb_missing_values_by_column)

def stationnaire(mdd1):
    for col in range(mdd1.shape[1]):
        mdd1[:, col][np.isnan(mdd1[:, col])] = np.nanmean(mdd1[:, col])
    return mdd1


def ecartMoyen(matrix1, matrix2):
    assert matrix1.shape == matrix2.shape, "As matrizes devem ter o mesmo tamanho"
    diferenca = matrix1 - matrix2
    soma_quadrados = np.sum(diferenca**2)
    return soma_quadrados



methode1 = stationnaire(mdd1)
em = ecartMoyen(digits.data,methode1)
print(em)


