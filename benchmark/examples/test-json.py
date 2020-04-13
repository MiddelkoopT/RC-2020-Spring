#!/usr/bin/python3

## This program demonstrates the use of JSON in Python.

import json

with open("test.json") as f:
    d=json.load(f)
    print(d)

