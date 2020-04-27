#!/bin/bash

for I in {1..100} ; do
    echo "=== $I"
    JOBS="$(squeue -h -u $USER |wc -l)"
    #echo $JOBS
    if [ $JOBS = 0 ] ; then
	echo done
	exit 0
    fi
    sleep 1
done

