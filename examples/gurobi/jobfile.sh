#!/bin/bash

#SBATCH -N 1
#SBATCH -c 4

echo "### gurobi SLURM $(hostname) ${SLURM_JOB_ID} $(date)"
. ./modules.sh

echo "+++ srun gurobi"
srun gurobi.sh ./gurobi-simple.py

echo "### gurobi SLURM $(hostname) ${SLURM_JOB_ID} $(date) done"
