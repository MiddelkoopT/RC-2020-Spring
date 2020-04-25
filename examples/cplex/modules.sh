#!/bin/bash

module load python/python-3.5.2
module load cplex-studio/cplex-studio-12.7.0

# Fix Python (use 3.5, not 2.7)
export PYTHONPATH=/cluster/software/cplex-studio/cplex-studio-12.7.0/cplex/python/3.5/x86-64_linux:$PYTHONPATH
