#!/bin/bash

#SBATCH -J CPLEX
#SBATCH -N 1
#SBATCH -c 4

echo '### SLURM' $(hostname) ${SLURM_JOB_ID}  $(date) 
module load cplex-studio/cplex-studio-12.7.0
module list

echo "+++ cplex"

srun python2 cplex-simple.py

