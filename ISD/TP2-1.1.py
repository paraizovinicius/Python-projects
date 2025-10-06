import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Créer un tableau de données
X = np.array([5.5, 6.0, 6.5, 6.0, 5.0, 6.5, 4.5, 5.0])
y = np.array([420, 380, 350, 400, 440, 380, 450, 420])

X = X.reshape(-1,1)
y = y.reshape(-1,1)

# Créer un modèle de régression linéaire
model = LinearRegression() # mettez fit_intercept=False dans les paramètres
model.fit(X, y)

coef = model.coef_
intercept = model.intercept_
squaredError = mean_squared_error(y, model.predict(X)) #Calculer l'erreur quadratique moyenne
CoefDetermination = r2_score(y, model.predict(X)) #Calculer le coefficient de détermination

print(f"Erreur quadratique moyenne: {squaredError}")
print(f"Coeficient de determination: {CoefDetermination}")


x_apprise = np.linspace(min(X), max(X), 100)
y_apprise = coef[0] * x_apprise + intercept

x_reg = np.linspace(X.min(), X.max(), 100)
y_reg = model.predict(x_reg.reshape(-1, 1))

plt.plot(x_apprise, y_apprise, color="red",label='Droite apprise')
plt.plot(x_reg, y_reg, color='green', label='Droite de régression')
plt.scatter(X, y, color="black") #Afficher les points de données
plt.show()


