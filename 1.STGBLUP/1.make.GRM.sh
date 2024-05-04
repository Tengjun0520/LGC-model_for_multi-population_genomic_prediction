#!/bin/sh

## pop1
gmat2 \
	--make-grm \
	--bfile ../0.example_data/OX \
	--out OX \
	--threads 30

## pop2	
gmat2 \
	--make-grm \
	--bfile ../0.example_data/UC \
	--out UC \
	--threads 30