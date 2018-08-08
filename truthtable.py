# Authors
# Damien Carver damien.carver@lip6.fr
# Hakan Metin   hakan.metin@lip6.fr

# Create a truth table for defined tests

import itertools
from tabulate import tabulate

class Model(object):
	"""docstring for Model"""
	def __init__(self, nargs, formulas):
		super(Model, self).__init__()
		self.nargs = nargs
		self.formulas = formulas

	def __str__(self):
		headers = [str(i) for i in range(self.nargs)] + [f.__name__ for f in self.formulas]
		res = []
		for variables in itertools.product(*[[False, True] for i in range(self.nargs)]):
			tmp = [v for v in variables]
			for f in self.formulas:
				tmp.append(f(*variables))
			res.append(tmp)
		return tabulate(res, headers=headers)
