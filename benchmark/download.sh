#!/bin/bash

install -dv data/
wget -c https://www.top500.org/lists/2019/11/download/TOP500_201911_all.xml -O data/top500.xml

md5sum -c data.md5

