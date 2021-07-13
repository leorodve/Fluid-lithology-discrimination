# Fluid-lithology-discrimination
Program using clustering algorithms to discriminate fluid/lithology

This program was tested with synthetic data of a well containing sands with gas. A crossplot of Vp and Rho versus the Impedance is useful to discriminate the sands containing gas from those who don't.
The value used to discriminate the sands with gas from other lithology was close to 17,000 [ft/s][g/cc].
Four different clustering algorithms were tested to see which one offered a better result.

<b>BIRCH\
<img src="https://i.imgur.com/oIn4hjN.png">
Minibatch K-means
<img src="https://i.imgur.com/IoVXSVm.png">
Agglomerative clustering
<img src="https://i.imgur.com/hLrlcvR.png">
Meanshift</b>
<img src="https://i.imgur.com/UrykvA5.png">

The results were compared using the Rand Index, testing the labels predicted agains't the true labels and the results are displayed on the next table:

| Clustering algorithm  | Vp-Impedance  | Rho-Impedance | Time(s)  |
|-------|-------|-----|-----|
| Birch | 1.0 | 1.0 | 0.0469  |
| Minibatch k-means | 0.875 | 1.0 | 0.0937  |
| Agglomerative clustering  | 0.946 | 1.0 | 0.0156  |
| Meanshift | 1.0 | 1.0 | 5.4218  |

Based on this, for this specific synthetic data, the BIRCH clustering algorithm yields the best results, with the highest score on the Rand Index and the second fastest performance time.
