#!/bin/sh

gmat2 \
    --mvlmm \
    --mgrm sig.agrm non_sig.agrm \
    --data ../0.example_data/all.pheno \
	--random id id \
    --trait tr_pop1 tr_pop2 \
    --out pop1_pop2 \
    --threads 30 \
    --predict
