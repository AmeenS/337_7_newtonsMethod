# Use Neton's method to determine which positions on the complex plane 
# converge to which root.
# 
# 
# AMS


from pylab import *
from numpy import *
from scipy.misc import imsave
import cmath
import os

r = 2.
w = 500
h = 500
tol = 1e-3

a = zeros((3, h, w))

red = a[0, :, :]
green = a[1, :, :]
blue  = a[2, :, :]

p1 = 1. + 0.j
p2 = complex(-0.5, sqrt(3.)/2.)
p3 = complex(-0.5, -sqrt(3.)/2.)

x = linspace(-r, r, w)
y = linspace(r, -r, h)
X, Y = meshgrid(x,y)

Z = X+Y*1.j

def whichRoot(Z):
  for i in range(10) :
    Z = 2./3.*Z + 1./(3.*Z*Z)
	
    red[abs(Z-p1) < tol]  += 1.
    green[abs(Z-p2) < tol] += 1.	
    blue[abs(Z-p3) < tol] += 1.
  imsave('z.png' , a)
  os.system('eog z.png&')


def rootPath( k, j):
  plot(p1.real, p1.imag, 'r*');	
  plot(p2.real, p2.imag, 'g*'); 	
  plot(p3.real, p3.imag, 'b*')
  plot([-r,r],[0,0], 'k-'); 	plot([0,0],[-r,r], 'k-')
  xlim(-r-.02,r+.02);		ylim(-r-.02,r+.02)
  plot(Z[k,j].real, Z[k,j].imag, 'ko')	

  for i in range(10) :
    Z[k,j] = 2./3.*Z[k,j] + 1./(3.*Z[k,j]*Z[k,j])
    xc = Z[k,j].real;	yc = Z[k,j].imag
    plot(xc, yc, 'ro',linestyle = '-',alpha = 7.0)	
    #print (xc,yc), '\t', abs(Z[k,j]-p1) < tol, '\t', abs(Z[k,j]-p2) < tol, '\t', abs(Z[k,j]-p3) < tol,
  show()

whichRoot(Z)
rootPath(250,185)






