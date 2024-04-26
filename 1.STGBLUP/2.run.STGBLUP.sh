#!/bin/sh

## pop1
gmat2 \
    --uvlmm \
    --grm pop1 \
    --data ../0.example_data/pop1.pheno \
    --trait tr_pop1 \
    --out tr_pop1 \
    --threads 30 \
    --predict
	
## pop2
gmat2 \
    --uvlmm \
    --grm all \
    --data ../0.example_data/pop2.pheno \
    --trait tr_pop2 \
    --out tr_pop2 \
    --threads 30 \
    --predict