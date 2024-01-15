2.2.4 - 

Datasets :

Le tuple contient (nb de clusters trouvées, score, temps d'execution)

### fourty.arff
cluster attendus: 40
```
silhouette_score:  (40, 0.7373305306497581, 8.302699327468872)
davies_bouldin_score:  (4, 0.994122842694181, 2.312343120574951)
calinski_harabasz_score:  (40, 5725.635045916126, 1.9695379734039307)
```
On voit que avec davies_bouldin_score  on n'arrive pas à avoir le bon nombre de clusters. 
Donc cette méthode n'est pas adapté à ce datasst en particulier.


### blobs.arff
cluster attendus: 3
```
silhouette_score:  (3, 0.559522406348139, 2.552882194519043)
davies_bouldin_score:  (6, 1.0973656666473668, 3.1535613536834717)
calinski_harabasz_score:  (3, 599.5022773042638, 2.2941720485687256)
```

### zelnik4.arff 
cluster attendus: 4
```
silhouette_score:  (12, 0.7281111684130831, 9.863889217376709)
davies_bouldin_score:  (2, 1.068820130652653, 2.675654411315918)
calinski_harabasz_score:  (49, 1330.419153613057, 3.153717517852783)
```


## 2.3 Limites de la méthode k-Means

Datasets avec possibles problèmes : 
- xor.arff
- target.arff
- spiral.arff

### xor.arff

```
silhouette_score:  (4, 0.4146171919647471, 7.999013662338257)
davies_bouldin_score:  (2, 1.1382222931618324, 2.39306640625)
calinski_harabasz_score:  (49, 1172.3130820168722, 2.1372861862182617)
```


### target.arff
```
silhouette_score:  (7, 0.5900437832053862, 9.050001621246338)
davies_bouldin_score:  (2, 1.1452260415270101, 3.3220341205596924)
calinski_harabasz_score:  (48, 1594.3156068226224, 2.6061604022979736)
```

### spiral.arff
```
silhouette_score:  (41, 0.5041217297201656, 8.28929328918457)
davies_bouldin_score:  (2, 1.1438673516450564, 2.6368701457977295)
calinski_harabasz_score:  (49, 1807.2203340832662, 3.0658204555511475)
```

Aucune méthode n'arrive à estimer un k pour ces datasets car l'algorithme de k-means 
n'arrive pas à clusteriser ces datasets car ces datasets ne sont pas convexes.

## 3 

Datasets intéressants : 
- target.arff
- silhouette.arff
- smile3.arff

### target.arff

```
distance max with descent:  {'min_dist': 0.19160733964158216, 'score': 0.441535204320492, 'exec_time': 0.6102066040039062, 'nb_cluster': 10}
distance max silhouette :  0.08  score :  0.4640996673022415  time :  1.5115585327148438  nb clusters :  205
distance max calinski :  0.01  score :  81586.14832761989  time :  0.3899397850036621  nb clusters :  737
distance max davies :  0.22  score :  11.228778763153235  time :  0.9198184013366699  nb clusters :  6
```

### spiral.arff

```
distance max with descent:  {'min_dist': 0.5999942227194687, 'score': 0.04067161576482462, 'exec_time': 0.574514627456665, 'nb_cluster': 2}
distance max with descent:  {'min_dist': 0.5999942227194687, 'score': 42.163840224091, 'exec_time': 0.13013291358947754, 'nb_cluster': 2}
distance max with descent:  {'min_dist': 0.5999942227194687, 'score': 4.530222967268666, 'exec_time': 0.1002194881439209, 'nb_cluster': 2}
distance max silhouette :  0.13  score :  0.04067161576482462  time :  2.1448416709899902  nb clusters :  2
distance max calinski :  0.04  score :  65.09600346384502  time :  0.4422616958618164  nb clusters :  890
distance max davies :  0.13  score :  4.530222967268666  time :  0.9955394268035889  nb clusters :  2
```


### smile3.arff

```
distance max silhouette :  0.03  score :  0.14210339590890306  time :  0.7028288841247559  nb clusters :  4
distance max calinski :  0.14  score :  80.74761000326659  time :  0.3325645923614502  nb clusters :  3
distance max davies :  0.03  score :  2.300714177241015  time :  0.33836936950683594  nb clusters :  4
```



###
- xor.arff / 