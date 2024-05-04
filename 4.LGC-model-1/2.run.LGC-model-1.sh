#!/bin/sh

gmat2 \
    --mvlmm \
    --mgrm sig.agrm non_sig.agrm \
    --data ../0.example_data/combined.pheno \
	--random id id \
    --trait TA.OX TA.UC \
    --out TA.lgc \
    --threads 30 \
    --predict
	