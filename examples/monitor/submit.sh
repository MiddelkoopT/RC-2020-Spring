#!/bin/bash

for I in {1..10} ; do
    echo $I
    sbatch jobfile.sh $I
done
