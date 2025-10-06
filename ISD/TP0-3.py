from sklearn import decomposition
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()

pca = decomposition.PCA(2)  # projection dans espace à deux axes (deux dimensions)
donnees_projetes = pca.fit_transform(digits.data)


plt.figure(figsize=(10, 6))
plt.scatter(donnees_projetes[:, 0], donnees_projetes[:, 1], c=digits.target, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('nipy_spectral', 10))
plt.xlabel('composante 1')
plt.ylabel('composante 2')
plt.colorbar()
plt.show()
