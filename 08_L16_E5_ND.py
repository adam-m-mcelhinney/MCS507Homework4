"""
HW4, #8
L16, #5

Consider the plot made by the script cubic_cylinder_cut.py,
done with matplotlib. Use gnuplot to make the same plot.



"""

# L-16 MCS 507 Wed 3 oct 2012 : cubic_cylinder_cut.py

# This script uses pyplot of matplotlib to plot
# the cubic cylinder z = x^3.

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

f = plt.figure()
a = f.gca(projection='3d',azim=-117,elev=15)
x = np.arange(-1,1,0.03)
y = np.arange(-1,1,0.03)
X, Y = np.meshgrid(x,y)
Z = X**3
for i in xrange(X.shape[0]):
  for j in xrange(X.shape[1]):
     if X[i,j]**2 < Y[i,j]: Z[i,j] = -1

#Create list of points to plot
x_1=[]
y_1=[]
z_1=[]
for i in range(len(X)):
    for j in range(len(X[i])):
        x_1.append(X[i][j])
        y_1.append(Y[i][j])
        z_1.append(Z[i][j])



path='C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507HW/MCS 507 Homework 4/MCS507Homework4/08_L16_E5_v2.dat'
file = open(path,'w+')
u = -1
v = -1
#n = 100
n = len(x_1)
file.write("# x y z c\n");
#for i in range(n+1):
for i in range(n):
   v = -1
   for j in range(n):
   #for j in range(n+1):
      file.write(str(x_1[j]) + " ")
      file.write(str(y_1[j]) + " ")
      file.write(str(z_1[j]) + " ")
      file.write(str(v) + "\n")
      v = v + 2.0/n
   file.write("\n")  # blank line
   u = u + 2.0/n
file.close()
