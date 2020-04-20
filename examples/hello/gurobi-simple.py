#!/usr/bin/python3

## based on http://www.gurobi.com/documentation/7.5/examples/mip1_py.html

"""
Maximize
  1 x1 + 2 x2
Subject To
  C1: x1 + x2 <= 40
  C2: 2 x1 + 1 x2 <= 60
Bounds
  x1 >= 0
  x2 >= 0
End

Solution
80
x1=0
x2=40
"""

from gurobipy import * 

debug=True

def log(message,isdebug=False):
    if (debug and isdebug) or isdebug==False:
        print('>',message)

m = Model("simple")
x1 = m.addVar(name="x1")
x2 = m.addVar(name="x2")
m.update()

print("x1:%s x2:%s" % (x1,x2))

m.setObjective(x1 + 2*x2, GRB.MAXIMIZE)

m.addConstr(x1 + x2 <= 40, "C1")
m.addConstr(2*x1 + x2 <= 60, "C2")

m.optimize()

print("Solution: %f" % (m.objVal,))
for v in m.getVars():
    print("%s:%f" % (v.varName, v.x))

#print(x1,x2,m.objVal)

assert x1.x==0.0      ## bad optimal solution
assert x2.x==40.0     ## bad optimal solution
assert m.objVal==80   ## bad optimal solution

log("Done: valid solution found")

