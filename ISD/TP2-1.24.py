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

# Transormer les données
h_transformed = h.reshape(-1,1)
c_transformed = c_sqrt.reshape(-1,1)
X = np.hstack((h_transformed, c_transformed))  # Ajouter h et c en un single input matrix

# Un nouveau modèle de regression
model = LinearRegression()
model.fit(X, c) 

# Les expérimentations précédentes
CoefDetermination = r2_score(c, model.predict(X))  #coefficient of determination
squaredError = mean_squared_error(c, model.predict(X))  # mean squared error

print(f"Mean Squared Error: {squaredError}")
print(f"Coefficient of determination: {CoefDetermination}")

# Les predictions
x_grid, y_grid = np.meshgrid(np.linspace(h.min(), h.max(), 100), np.linspace(c.min(), c.max(), 100))
z_grid = model.predict(np.hstack((x_grid.reshape(-1, 1), np.sqrt(y_grid.reshape(-1, 1)))))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(h, c, c_sqrt, c='black')
ax.plot_surface(x_grid, y_grid, z_grid.reshape(x_grid.shape), color='red', alpha=0.5)  # Regression surface

plt.show()