# IMSE 8410 HPC Clusters

*IMSE 8410 Advanced Computational Systems and Data Engineering*

Material Copyright 2017-2020 by Timothy Middelkoop. Source code
licensed under the Apache License, Version 2.0. Documentation licensed
under CC by SA 3.0.

## High Performance Computing (HPC) Clusters

> "It does not fit on my laptop. Now what?"

## Objectives

In this module we will learn about High Performance Computing (HPC)
clusters and specifically the SLURM cluster workload management
system.  By the end of this module students should be able to do the following:

1. Describe the basics of a cluster and a workload manager.
2. Determine what resources are available on the cluster and their
   status (nodes, partitions, jobs and the queue, and priority) by
   using `sinfo`, `squeue`, `scontrol`, `sshare`, and `sacctmgr`.
3. Show the status and resource utilization of previous jobs (`sacct`)
4. Show summary information about cluster utilization users and
   accounts using `sreport`.
5. Use the `srun` command to run interactive jobs.
6. Create simple jobfiles and use `sbatch` to submit them.
7. Specify job resources (time, memory, cores, nodes, tasks).
8. Run multi-core and multi-node test jobs.  Understand the difference
   between 'multi-task', 'multi-core', and 'multi-node' jobs and how to specify them.
9. Use the `SLURM_` environment variables to show information about the
   current job and task.

## Reading

Required Reading
 * High Performance Computing: Modern Systems and Practices (Chapter 5, The Essential Resource Management)
 * HPC Carpentry (Scheduler): https://hpc-carpentry.github.io/hpc-intro/13-scheduler/index.html

Additional Resources
 * SLURM Workload Manager: https://slurm.schedmd.com/quickstart.html
 * HPC Carpentry: https://hpc-carpentry.github.io/hpc-intro/

