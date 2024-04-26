#!/bin/sh

## trait combined
gmat2 \
    --uvlmm \
    --grm all \
    --data ../0.example_data/all.pheno \
    --trait tr_merge \
    --out tr_merge \
    --threads 30 \
    --predict
	