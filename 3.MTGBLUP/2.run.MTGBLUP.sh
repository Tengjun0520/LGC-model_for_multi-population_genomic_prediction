#!/bin/sh

gmat2 \
    --mvlmm \
    --grm combined \
    --data ../0.example_data/combined.pheno \
    --trait TA.OX TA.UC \
    --out TA.mtgblup \
    --threads 30 \
    --predict
	