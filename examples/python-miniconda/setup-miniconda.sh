#!/bin/bash
set -e

. ./modules.sh

# Hack on some systems that fail the first time on a conda run
install -dv ~/.conda/pkgs/cache

conda create --yes --prefix ./conda python=3.8

source activate ./conda
conda install --yes conda

