"""
HW4, #8
L16, #5

Consider the plot made by the script cubic_cylinder_cut.py,
done with matplotlib. Use gnuplot to make the same plot.

ASK PROF, COMPLETELY STUCK

"""

### L-16 MCS 507 Wed 3 oct 2012 : cubic_cylinder_cut.py
##
### This script uses pyplot of matplotlib to plot
### the cubic cylinder z = x^3.
##
##from mpl_toolkits.mplot3d import Axes3D
##from matplotlib import cm
##import matplotlib.pyplot as plt
##import numpy as np
##
##f = plt.figure()
##a = f.gca(projection='3d',azim=-117,elev=15)
##x = np.arange(-1,1,0.03)
##y = np.arange(-1,1,0.03)
##X, Y = np.meshgrid(x,y)
##Z = X**3
##for i in xrange(X.shape[0]):
##  for j in xrange(X.shape[1]):
##     if X[i,j]**2 < Y[i,j]: Z[i,j] = -1
##
##s = a.plot_surface(X,Y,Z,rstride=1,cstride=1,
##                   cmap=cm.jet,linewidth=0)
##f.colorbar(s,shrink=0.5)
##
##plt.show()


set pm3d implicit at s
set xlabel "X axis"
set xrange [ -1 : 1] noreverse nowriteback
set ylabel "Y axis"
set yrange [ -1 : 1] noreverse nowriteback
set zlabel "Z axis"
set zrange [ -1 : 1] noreverse nowriteback


z(x)=x**3
f(y)=y**2
y(z)=z**2


splot z(x), f(y)
splot x**3, y**(1/2.), -y**(1/2.)
