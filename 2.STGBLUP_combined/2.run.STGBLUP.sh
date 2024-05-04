#!/bin/sh

## trait combined
gmat2 \
    --uvlmm \
    --grm combined \
    --data ../0.example_data/combined.pheno \
    --trait TA.combined \
    --out TA.combined \
    --threads 30 \
    --predict
	