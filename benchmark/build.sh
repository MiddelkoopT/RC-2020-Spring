#!bin/bash
set -e

. ./modules.sh

install -dv ./build/

if [ ! -f build/hpl-2.3.tar.gz ] ; then
    (
	cd build
	wget -c  https://www.netlib.org/benchmark/hpl/hpl-2.3.tar.gz
	tar -xzf hpl-2.3.tar.gz
    )
fi

PROJECTHOME=$PWD

echo "=== Building in $PROJECTHOME $(date) $(hostname)"
( cd build/hpl-2.3 && ./configure --prefix=${PROJECTHOME}/local && make && make install )

echo "=== Build Done $(date)"

