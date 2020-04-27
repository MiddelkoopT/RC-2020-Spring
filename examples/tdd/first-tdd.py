#!/usr/bin/python

"""
Red:
Green:
Refactor:
"""

"""
add: 3+4=7
"""

assert True  ## This should pass
#assert False ## This should through an assersion.

assert True==True  ## This should pass
#assert True==False ## This should fail
assert 3+4==7      ## Add test

def add(a1,a2):
    #print(a1,a2)
    return a1+a2

assert add(3,4)==7 ## Add failed
assert add(1,2)==3 ## Add failed
assert add(-1,-2)==-3 ## Add failed
#assert add("1","2")==3 ## Add failed
