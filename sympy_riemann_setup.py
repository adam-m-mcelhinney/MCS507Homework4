# L-16 MCS 507 Wed 3 Oct 2012 : sympy_riemann_setup.py

# This script prepares the setup to plot the Riemann surface with gnuplot
# for the cubed root, defined as z = (u + I*v)**3.

from sympy import *
u, v = symbols('u,v', real=True)
var('w,z')
w = u + I*v
z = w**3
e_z = expand(z)
print e_z
rp = re(e_z)
print rp
ip = im(e_z)
print ip

# We will plot the surface defined by 
# [re((u+I*v)**3), im((u+I*v)**3, u]
# so the height is the real part of the cubed root.

from sympy.utilities import lambdify
s = "[" + str(rp) + "," + str(ip) + "," + str(u) + "]"
import numpy
f = lambdify((u,v),s,numpy)
print f(3,2)

# If matplotlib is installed, then we can plot surfaces
# with the visualization module of the package sympy.mpmath.
# We use splot to plot the surface given in parametric form 
# by f as f(u,v) = x, y, z, for u and v in [-1,+1]

# from sympy.mpmath import splot
# splot(f,[-1,1],[-1,1])

# We sample the surface for u and v ranging in [-1,+1]
# where u is the real part of z^(1/3) and v the imaginary part of z^(1/3).
# The plot shows the real part as the height and uses the color
# as the imaginary part.
# The order of the enumeration of the sample points goes first with v
# and then with u.  This produces a correct plot.
path='C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507HW/MCS 507 Homework 4/MCS507Homework4/08_L16_E5.dat'
file = open(path,'w')
u = -1
v = -1
n = 100
file.write("# x y z c\n");
for i in range(n+1):
   v = -1
   for j in range(n+1):
      x,y,z = f(u,v)
      file.write(str(x) + " ")
      file.write(str(y) + " ")
      file.write(str(z) + " ")
      file.write(str(v) + "\n")
      v = v + 2.0/n
   file.write("\n")  # blank line
   u = u + 2.0/n
file.close()

# gnuplot> splot "/tmp/riemann.dat" u 1:2:3:4 with pm3d
# The mouse bindings to change the view do not work with AquaTerm.
# To change the view do:
# gnuplot> set view 60, 130, 1, 1
# gnuplot> replot
# gnuplot> set view 75, 120, 1, 1
# gnuplot> replot

