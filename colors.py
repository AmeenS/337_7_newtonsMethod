# Representing a color image by a 3D array using scipy
#
#
# AMS

from numpy import *
from scipy.misc import imsave
import os


h = 600
w = 800
a = zeros((3,h,w))

a[ 0, :400, :600 ] = 1.		
""" first value is color the number its equal to in intensity."""
a[ 2, 100:500, 300:780 ] = 1.
a[ 1, 200:600, :400] = 1.

imsave('foo.png', a)

os.system('eog foo.png&') # ANY terminal command can be executed this way
