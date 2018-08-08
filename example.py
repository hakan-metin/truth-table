#!/usr/bin/env python

# Authors
# Damien Carver damien.carver@lip6.fr
# Hakan Metin   hakan.metin@lip6.fr

# Create a truth table for defined tests

from truthtable import Model

# Functions

def eq(a, b):
        return (a and b) or (not a and not b)

def le(a, b):
        return a or not b

def lt(a, b):
        return a and not b

def implies(a, b):
        return not a or b

# Formulas

def a_le_b(*args):
	a, b, c = args
	return le(a, b)

def a_eq_b_implie_b_le_c(*args):
	a, b, c = args
	return implies(a == b, le(b, c))

def a_lt_b_implie_b_le_c(*args):
	a, b, c = args
	return implies(lt(a, b), le(b, c))

def mininal(*args):
	return a_le_b(*args) and a_eq_b_implie_b_le_c(*args) and a_lt_b_implie_b_le_c(*args)

formulas = [a_le_b, a_eq_b_implie_b_le_c, a_lt_b_implie_b_le_c, mininal]
print(Model(3,formulas))
