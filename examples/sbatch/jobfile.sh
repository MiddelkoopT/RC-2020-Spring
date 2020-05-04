#!/bin/bash

#SBATCH -n 3

echo "=== $(hostname) $(date) ${SLURM_JOB_ID}"
srun /bin/echo Hello $(hostname)
srun -n 2 /bin/echo Two $(hostname)
