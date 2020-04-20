#!/bin/bash

#SBATCH -N 1
#SBATCH -c 4

echo '### SLURM' $(hostname) ${SLURM_JOB_ID} $(date)
module load gurobi/gurobi-9.0.1
module list

echo "+++ gurobi"
srun gurobi.sh ./gurobi-simple.py
