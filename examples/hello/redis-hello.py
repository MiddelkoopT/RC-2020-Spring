#!/usr/bin/python3

## Install and run a server - for example:
# conda install -y redis redis-py

## Start server with
# redis-server &
## Stop server with
# kill %redis-server

import redis
import json

## Connect to server use 'decode_responses=True' if all keys are strings
db=redis.Redis()

## Read/write simple binary
db.set("one",1)
print(db.get("one"))

## Store as utf-8 encoded json.
db.set("two",json.dumps([1,2,3]))
v=db.get("two")
d=json.loads(v)
print(d)

