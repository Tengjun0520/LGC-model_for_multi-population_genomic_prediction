#!/bin/sh

gmat2 \
    --mvlmm \
    --grm all \
    --data ../0.example_data/all.pheno \
    --trait tr_pop1 tr_pop2 \
    --out pop1_pop2 \
    --threads 30 \
    --predict
	