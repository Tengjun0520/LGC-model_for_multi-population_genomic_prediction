#!/bin/sh

gmat2 \
    --mvlmm \
    --mgrm lgc_pos.agrm lgc_neg.agrm lgc_res.agrm \
    --data ../0.example_data/all.pheno \
	--random id id id \
    --trait tr_pop1 tr_pop2 \
    --out pop1_pop2 \
    --threads 30 \
    --predict
	
