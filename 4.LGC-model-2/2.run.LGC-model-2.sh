#!/bin/sh

gmat2 \
    --mvlmm \
    --mgrm lgc_pos.agrm lgc_neg.agrm lgc_res.agrm \
    --data ../0.example_data/combined.pheno \
	--random id id id \
    --trait TA.OX TA.UC \
    --out TA.lgc \
    --threads 30 \
    --predict
	