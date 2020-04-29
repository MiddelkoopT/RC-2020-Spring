#!/bin/bash


echo "=== $(hostname) $(date)"

echo "$(jq -r .data config.json)"

