#!/bin/bash

. ./environment.sh

cat > config.json <<EOF
{
    "data": "$DATA",
    "scratch": "$SCRATCH"
}
EOF
