from sklearn import decomposition
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()

pca = decomposition.PCA(n_components=3)
donnees_projetes = pca.fit_transform(digits.data)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(projection='3d')
scatter = ax.scatter(donnees_projetes[:, 0], donnees_projetes[:, 1], donnees_projetes[:, 2], c=digits.target, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('nipy_spectral', 10))
ax.set_xlabel('composante 1')
ax.set_ylabel('composante 2')
ax.set_zlabel('composante 3')
plt.colorbar(scatter)
plt.show()
