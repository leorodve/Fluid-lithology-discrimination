# Fluid lithology discrimination

Program using clustering algorithms to discriminate fluid/lithology.

### Table of Contents
* [Installation](https://github.com/leorodve/fluid-lithology-discrimination#installation)
  * [Linux](https://github.com/leorodve/fluid-lithology-discrimination#linux)
    * [Install](https://github.com/leorodve/fluid-lithology-discrimination#install)
* [Examples](https://github.com/leorodve/fluid-lithology-discrimination#examples)
* [License & Contributing](https://github.com/leorodve/fluid-lithology-discrimination#license-and-contributing)
* [Authors](https://github.com/leorodve/fluid-lithology-discrimination#Authors)

## Installation
### Linux
### Install
You can download the latest version of the source code from [GitHub](https://github.com/leorodve/fluid-lithology-discrimination) or if you have ```git``` installed, you can use the following command:
```bash
git clone https://github.com/leorodve/fluid-lithology-discrimination.git
```
Change your directory to the newly created containing the source code and run:
```bash
python well_data_clustering.py
```
## Examples
This program was tested with synthetic data of a well containing sands with gas.

A crossplot of Vp and Rho versus the Impedance is useful to discriminate the sands containing gas from those who don't.
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
## License and contributing
Licensed under the [GPL-3.0](http://www.gnu.org/licenses/gpl-3.0.html) License.

All kinds of contributions, including code, bug reports and issues are welcomed.

## Authors
Made by Leonardo Rodriguez.
