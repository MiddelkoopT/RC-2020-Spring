#!/usr/bin/python3

"""
Maximize
      1 x1 + 2 x2
Subject To
  C1:   x1 +   x2 <= 40
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

import cplex

m = cplex.Cplex()
m.objective.set_sense(m.objective.sense.maximize)

inf = cplex.infinity

names =     [ "x1", "x2"]
objective = [   1 ,   2 ]
lower =     [   0 ,   0 ]
upper =     [ inf , inf ]

m.variables.add(obj = objective,
                lb = lower,
                ub = upper,
                names = names)

constraint_names = ["C1", "C2"]
constraints = [
    [[ "x1", "x2" ] , [ 1, 1] ],
    [[ "x1", "x2" ] , [ 2, 1] ]
]
sign = ["L", "L"]
rhs  = [ 40, 60 ]

m.linear_constraints.add(lin_expr = constraints,
                         senses = sign,
                         rhs = rhs,
                         names = constraint_names)

print("+++ Solving")
m.solve()

print("+++ Solution")
print(m.solution.get_values())
print(m.solution.get_objective_value())

print("+++ Validate")
assert [0,40.0]==m.solution.get_values()    ## Solution values failed.
assert m.solution.get_objective_value()==80 ## Objective value failed.

