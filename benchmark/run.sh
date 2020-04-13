#!/bin/bash

PROJECT_CONFIG=config.json

echo "=== $(date) $(hostname) ${PROJECT_CONFIG}"

. ./environment.sh


echo "=== $(date) $(hostname) start"

python3 ./preprocess.py ${PROJECT_CONFIG}
Rscript ./analysis.R ${PROJECT_CONFIG}


echo "=== $(date) $(hostname) done"
