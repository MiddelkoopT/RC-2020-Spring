#!/bin/bash

unset MODULEPATH
unset MODULESHOME

. spack/share/spack/setup-env.sh

. $(spack location -i environment-modules)/init/bash

