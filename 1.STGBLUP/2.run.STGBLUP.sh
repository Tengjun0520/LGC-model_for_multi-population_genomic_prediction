#!/bin/sh

## pop1
gmat2 \
    --uvlmm \
    --grm OX \
    --data ../0.example_data/OX.pheno \
    --trait TA \
    --out TA_OX \
    --threads 30 \
    --predict
	
## pop2
gmat2 \
    --uvlmm \
    --grm UC \
    --data ../0.example_data/UC.pheno \
    --trait TA \
    --out TA_UC \
    --threads 30 \
    --predict