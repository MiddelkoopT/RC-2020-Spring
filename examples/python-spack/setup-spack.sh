#!/bin/bash

git clone https://github.com/spack/spack.git

unset MODULEPATH
unset MODULESHOME
. spack/share/spack/setup-env.sh

spack bootstrap

spack install python@3.8.2
spack load python@3.8.2

python3 -m ensurepip
pip3 install --upgrade pip
