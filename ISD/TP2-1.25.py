import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

# Charger les données
texto = np.loadtxt("C:\\Users\\parai\\Downloads\\eucalyptus.txt")
h = texto[:, 0]
c = texto[:, 1]
c_sqrt = np.sqrt(c)
c_carre = np.power(c,2)

# Transormer les données
h_transformed = h.reshape(-1,1)
c_sqrtT = c_sqrt.reshape(-1,1)
c_carreT = c_carre.reshape(-1,1)
X_poly = np.hstack((h_transformed, c_sqrtT, c_carreT))  # Ajouter tout en X


# Ajuster avec les nouvelles caractéristiques
model_poly = LinearRegression()
model_poly.fit(X_poly, c)

#Calculer la MSE et R2
mse_scores_poly = cross_val_score(model_poly, X_poly, c, scoring='neg_mean_squared_error', cv=5)
r2_scores_poly = cross_val_score(model_poly, X_poly, c, scoring='r2', cv=5)

print(f"Cross-validated MSE: {-mse_scores_poly.mean()}")
print(f"Coeficient de determination: {r2_scores_poly.mean()}")