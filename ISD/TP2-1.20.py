import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

texto = np.loadtxt("C:\\Users\\parai\\Downloads\\eucalyptus.txt")
h = texto[:, 0]
c = texto[:, 1]

h = h.reshape(-1,1)
c = c.reshape(-1,1)

# Créer un modèle de régression linéaire
model = LinearRegression() 
model.fit(h, c)

coef = model.coef_
intercept = model.intercept_
CoefDetermination = r2_score(c, model.predict(h)) #Calculer le coefficient de détermination
squaredError = mean_squared_error(c, model.predict(h)) #Calculer l'erreur quadratique moyenne

print(f"Erreur quadratique moyenne: {squaredError}")
print(f"Coeficient de determination: {CoefDetermination}")


h_pred = coef[0] * 22.8 + intercept # Calculer la valeur de hauteur prédite pour une circonférence de 22.8


print(f"Hauteur prédite: {h_pred}")

x_apprise = np.linspace(h.min(), h.max(), 100)
y_apprise = coef[0] * x_apprise + intercept

x_reg = np.linspace(h.min(), h.max(), 100)
y_reg = model.predict(x_reg.reshape(-1, 1))

plt.plot(x_apprise, y_apprise, color="red",label='Droite apprise')
plt.plot(x_reg, y_reg, color='green', label='Droite de régression')
plt.scatter(h, c, color="black") #Afficher les points de données

plt.show()