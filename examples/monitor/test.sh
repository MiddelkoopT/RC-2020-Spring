#!/bin/bash


for I in {1..10} ; do
    echo "=== $I"
    if [ ! -r run-${I}.txt ] ; then
	echo "+++ $I missing"
    fi
done


