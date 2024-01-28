import numpy as np
import scipy.cluster.hierarchy as shc
import time
from scipy.io import arff
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score, euclidean_distances


def k_agglo_find(dataset, f) -> (int, float, float):
    current_time = time.time()
    k_max = 0
    score_max = 0
    for k in range(2,50):
        model = AgglomerativeClustering(linkage='single', n_clusters=k)
        model.fit(dataset)
        score = f(dataset, model.labels_)
        if score > score_max:
            score_max = score
            k_max = k
    end_time = time.time()
    executing_time = end_time - current_time
    return k_max, score_max, executing_time

def find_min_dist(dataset, f):
    res = {}
    nb_clusterts = {}
    def distance_loss(dist):
        model = AgglomerativeClustering(distance_threshold=dist, linkage='single', n_clusters=None)
        model.fit(dataset)
        if model.n_clusters_ == 1 or model.n_clusters_ > 999 or len(model.labels_) > len(dataset) - 1:
            score = -1000000.
            print("eval 1 :", dist)
        else:
            score = f(dataset, model.labels_)
        res[dist] = score
        nb_clusterts[dist] = model.n_clusters_
        return -score

    bounds = (0.001, 50)
    current_time = time.time()
    min_dist = minimize_scalar(distance_loss, bounds=bounds, method="bounded").x
    end_time = time.time()
    executing_time = end_time - current_time

    return {"min_dist": min_dist,
            "score": res[min_dist],
            "exec_time": executing_time,
            "nb_cluster": nb_clusterts[min_dist]
            }


def loop_cluster(data, f):
    distance_threashold_max = 0
    score_max = 0
    nb_clusters_max = 0
    start = time.time()
    for dist in range(100, 1000):
        model = AgglomerativeClustering(distance_threshold=dist/100, linkage='single', n_clusters=None)
        model.fit(data)
        if (model.n_clusters_ != 1 and model.n_clusters_ < 1000):
            score = f(data, model.labels_)
            if score > score_max:
                score_max = score
                distance_threashold_max = dist
                nb_clusters_max = model.n_clusters_
    end = time.time()
    return distance_threashold_max/100, score_max, end - start, nb_clusters_max


path = './tp-clustering/clustering-benchmark/src/main/resources/datasets/artificial/'
# Datasets intéressants : blobs.arff (k = 3)/fourty (k = 40)/zelnik4 (k = 4)
databrut = arff.loadarff(open(path + "zelnik4.arff", 'r'))
datanp = np.array([[x[0], x[1]] for x in databrut[0]])
f0 = datanp[:, 0]  # tous les elements de la premiere colonne
f1 = datanp[:, 1]  # tous les elements de la deuxieme colonne

# Donnees dans datanp
print("Dendrogramme 'single' donnees initiales")
linked_mat = shc.linkage(datanp, 'complete')
plt.figure(figsize=(12, 12))
shc.dendrogram(linked_mat, orientation='top', distance_sort='descending', show_leaf_counts=False)
plt.show()

# set distance_threshold (0 ensures we compute the full tree)
tps1 = time.time()
model = AgglomerativeClustering(linkage='single', n_clusters=6)
model = model.fit(datanp)
tps2 = time.time()
labels = model.labels_
k = model.n_clusters_
leaves = model.n_leaves_

# Display clustering
plt.scatter(f0, f1, c=labels, s=8)
plt.title("Resultat du clustering")
plt.show()
print("nb clusters =", k, ", nb feuilles =", leaves, "runtime =", round((tps2 - tps1) * 1000, 2), "ms")

# set the number of clusters
k = 4
tps1 = time.time()
model = AgglomerativeClustering(linkage='complete', n_clusters=k)
model = model.fit(datanp)
tps2 = time.time()
labels = model.labels_
kres = model.n_clusters_
leaves = model.n_leaves_

print("distance max with descent: ", find_min_dist(datanp, silhouette_score))
print("distance max with descent: ", find_min_dist(datanp, calinski_harabasz_score))
print("distance max with descent: ", find_min_dist(datanp, davies_bouldin_score))

silhouette_score_result = loop_cluster(datanp, silhouette_score)
print("distance max silhouette : ", silhouette_score_result[0], " score : ", silhouette_score_result[1], " time : ", silhouette_score_result[2], " nb clusters : ", silhouette_score_result[3])

calinski_harabasz_result = loop_cluster(datanp, calinski_harabasz_score)
print("distance max calinski : ", calinski_harabasz_result[0], " score : ", calinski_harabasz_result[1], " time : ", calinski_harabasz_result[2], " nb clusters : ", calinski_harabasz_result[3])

davies_bouldin_result = loop_cluster(datanp, davies_bouldin_score)
print("distance max davies : ", davies_bouldin_result[0], " score : ", davies_bouldin_result[1], " time : ", davies_bouldin_result[2], " nb clusters : ", davies_bouldin_result[3])

print("k agglomerate silhouette_score: ", k_agglo_find(datanp, silhouette_score))
print("k agglomerate: calinski_harabasz_result", k_agglo_find(datanp, calinski_harabasz_score))
print("k agglomerate: davies_bouldin_score", k_agglo_find(datanp, davies_bouldin_score))