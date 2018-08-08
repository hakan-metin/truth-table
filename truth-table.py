#!/usr/bin/env python

# Authors
# Damien Carver damien.carver@lip6.fr
# Hakan Metin   hakan.metin@lip6.fr

# Create a truth table for defined tests

import itertools
from tabulate import tabulate

def eq(a, b):
        return (a and b) or (not a and not b)

def le(a, b):
        return a or not b

def lt(a, b):
        return a and not b

def implies(a, b):
        return not a or b

def a_le_b(*args):
	return le(a, b)

def a_eq_b_implie_b_le_c(*args):
	return implies(a == b, le(b, c))

def mininal(*args):
        return a_le_b(a, b, c) and a_eq_b_implie_b_le_c(a, b, c)

Bool = [False, True]
tests = [a_le_b, a_eq_b_implie_b_le_c, mininal]
headers = ['a', 'b', 'c'] + [t.__name__ for t in tests]

res = []
for a, b, c in itertools.product(Bool, Bool, Bool):
	tmp = [a, b, c]
	for test in tests:
		tmp.append(test(a,b,c))
	res.append(tmp)
print(tabulate(res, headers=headers))
