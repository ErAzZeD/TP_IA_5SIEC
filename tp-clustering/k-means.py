import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn import cluster
from scipy.io import arff

#
# Les donnees sont dans datanp ( 2 dimensions )
# f0 : valeurs sur la premiere dimension
# f1 : valeur sur la deuxieme dimension
#
path = './clustering-benchmark/src/main/resources/datasets/artificial/'
databrut = arff.loadarff(open(path + "spiral.arff", 'r'))
datanp = np.array([[x[0], x[1]] for x in databrut[0]])
f0 = datanp[:, 0]  # tous les elements de la premiere colonne
f1 = datanp[:, 1]  # tous les elements de la deuxieme colonne
plt.scatter(f0, f1, s=8)

print("Appel KMeans pour une valeur fixee de k")
tps1 = time.time()
k = 4
model = cluster.KMeans(n_clusters=k, init='k-means++')
model.fit(datanp)
tps2 = time.time()
labels = model.labels_
iteration = model.n_iter_
plt.scatter(f0, f1, c=labels, s=8)
plt.title("Donnees apres clustering Kmeans")
plt.show()
print("nb clusters = ", k, ", nb iter = ", iteration, " , ...... runtime = ", round((tps2 - tps1) * 1000, 2), " ms ")
