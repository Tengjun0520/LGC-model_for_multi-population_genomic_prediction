# multi-population genomic prediction

## Model summary

We present two novel methods for integrating between-population LGC information into multi-population genomic prediction, which based on the MTGBLUP framework and involve grouping SNPs according to the significance or degree of local genetic correlations of the regions in which they are located. The models is as follows,
![](https://github.com/Tengjun0520/multi-population_genomic_prediction/blob/main/model.png)

## Requirements

- [GMAT](https://github.com/chaoning/GMAT)
- [PLINK](https://www.cog-genomics.org/plink/)
- [Python 3.11](https://www.python.org/)

## Example data

There are genotype and phenotype data for two populations as example data (450 individuals in the population 1, 50 individuals in the population 2), which can be used to run all scripts.

## How to run script

Taking LGC-model-1 as an example,

### Step 1: calculate the genomic relationship matrix (GRM)

python3 1.make.GRM.py

### Step 2: run LGC-model-1

bash 2.run.LGC-model-1.sh

### Step 3: calculate the total genomic estimated breeding values (GEBV)

python3 3.merge_gebv.py

## About

If you want to know more details about the model, please read this paper

Jun Teng, Tingting Zhai, Xinyi Zhang, Changheng Zhao, Wenwen Wang, Hui Tang, Dan Wang, Yingli Shang, Chao Ning* and Qin Zhang*. Improving multi-population genomic prediction accuracy using multi-trait GBLUP models which incorporate global or local genetic correlation information. Briefings in Bioinformatics. in press.
