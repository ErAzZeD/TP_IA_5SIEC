import time

import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics
from sklearn import cluster
from scipy.io import arff
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score


# def k_mean_silouette(dataset) -> (int, float, :
#     max_score = 0
#     k = 0
#
#     for i in range(50):
#         model = cluster.KMeans(n_clusters=i, init='k-means++')
#         model.fit(datanp)
#         score = silhouette_score(datanp, model.labels_)
#         if score > max_score:
#             max_score = score
#             k = i
#     return k


def k_mean_find(dataset, f) -> (int, float, float):
    current_time = time.time()
    k_max = 0
    score_max = 0
    for k in range(2,50):
        model = cluster.KMeans(n_clusters=k,init='k-means++', n_init=10)
        model.fit(dataset)
        score = f(dataset, model.labels_)
        if score > score_max:
            score_max = score
            k_max = k
    end_time = time.time()
    executing_time = end_time - current_time
    return k_max, score_max, executing_time

# Parser un fichier de donnees au format arff
# data est un tableau d ’ exemples avec pour chacun
# la liste des valeurs des features
#
# Dans les jeux de donnees consideres :
# il y a 2 features ( dimension 2 )
# Ex : [[ - 0 . 499261 , -0 . 0612356 ] ,
# [ - 1 . 51369 , 0 . 265446 ] ,
# [ - 1 . 60321 , 0 . 362039 ] , .....
# ]
#
# Note : chaque exemple du jeu de donnees contient aussi un
# numero de cluster . On retire cette information
path = './clustering-benchmark/src/main/resources/datasets/artificial/'
# Datasets intéressants : blobs.arff (k = 3)/fourty (k = 40)/zelnik4 (k = 4)
databrut = arff.loadarff(open(path + "smile3.arff", 'r'))
datanp = np.array([[x[0], x[1]] for x in databrut[0]])
# Affichage en 2D
# Extraire chaque valeur de features pour en faire une liste
# Ex pour f0 = [ - 0 . 499261 , -1 . 51369 , -1 . 60321 , ...]
# Ex pour f1 = [ - 0 . 0612356 , 0 . 265446 , 0 . 362039 , ...]
f0 = datanp[:, 0]  # tous les elements de la premiere colonne
f1 = datanp[:, 1]  # tous les elements de la deuxieme colonne
plt.scatter(f0, f1, s=8)
plt.title("Donnees initiales")
plt.show()

print(" Appel KMeans pour une valeur fixee de k ")
tps1 = time.time()
k = 40
model = cluster.KMeans(n_clusters=k, init='k-means++')
model.fit(datanp)
tps2 = time.time()
labels = model.labels_
iteration = model.n_iter_
plt.scatter(f0, f1, c=labels, s=8)
plt.title(" Donnees apres clustering Kmeans ")
plt.show()
print(" nb clusters = ", k, " , nb iter = ", iteration, " ,runtime = ", round((tps2 - tps1) * 1000, 2),
      " ms / Silhouette score : ", silhouette_score)

print("silhouette_score: ", k_mean_find(datanp, silhouette_score))
print("davies_bouldin_score: ", k_mean_find(datanp, davies_bouldin_score))
print("calinski_harabasz_score: ", k_mean_find(datanp, calinski_harabasz_score))

