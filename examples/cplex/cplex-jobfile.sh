#!/bin/bash

#SBATCH -J CPLEX
#SBATCH -N 1
#SBATCH -c 4

. ./modules.sh
echo '### SLURM' $(hostname) ${SLURM_JOB_ID}  $(date) 

echo "+++ cplex"

srun python3 cplex-simple.py


