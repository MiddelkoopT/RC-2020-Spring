#!/bin/bash

. ./environment.sh

echo "=== Install R libraries"
install -dv ${R_LIBS_USER}
Rscript setup.R

echo "=== Download data"
bash ./download.sh


