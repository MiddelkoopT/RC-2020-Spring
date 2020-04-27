#!/bin/bash

echo "=== monitor $(hostname) $(date) $1"

sleep 60
touch run-${1}.txt

echo "=== monitor $(hostname) $(date) $1 done"

