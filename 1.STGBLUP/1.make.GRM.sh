#!/bin/sh

## pop1
gmat2 \
	--make-grm \
	--bfile ../0.example_data/pop1 \
	--out pop1 \
	--threads 30

## pop2	
gmat2 \
	--make-grm \
	--bfile ../0.example_data/pop2 \
	--out pop2 \
	--threads 30
