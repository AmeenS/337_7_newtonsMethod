# Function to implement Newtons method. Sample values used
#
# AMS

# import sys
# f = sys.argv[1]
# df = sys.argv[2]


from math import *
from numpy import *


def newton ( f, df, x, tol):
	count = 0
	while True:
		s = -f(x)/df(x) # our Newton step
		x = x +s
		count += 1 
		if abs(s) <= tol: break
	return x, s, count

def newNew(f, df, x, tol):
	s = -f(x)/df(x)
	x1 = x+s
	return abs(x1 - x)

def f(x):
	return tanh(x)
def df(x):
	return 1-(tanh(x)*tanh(x))

print newNew (f, df, .0002, 1e-10)

#print golden( f, 1.5)

""" Incredibly efficient and applicible algorithm. Know for life. """
