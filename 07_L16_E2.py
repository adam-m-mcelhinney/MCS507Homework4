"""
HW4, #7
L16, #2
(x = r cos(4t), y = r sin(4t), z = sin(7t)) with r = 2 + 4/5 cos(7t)
deﬁnes a torus knot. Plot this knot, for t ∈ [0, 2π]. Make 4 subplots
for t ∈ [0, 2kπ/4], for k = 1,2,3,4.

Done

"""


# This script uses pyplot to show the twisted cubic,
# a space curve defined by x = t, y = t^2, z = t^3.

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import cos, sin
import matplotlib.pyplot as plt
from math import pi #, cos, sin


t = np.linspace(0,2*pi,100)
r= 2+(4/5.)*cos(7*t)

x = r*cos(4*t)
y = r*sin(4*t)
z = sin(7*t)
# open a new figure window
f = plt.figure()
# get current axes of the figure
a = f.gca(projection='3d')
# plot the sampled points
a.plot(x,y,z,label='Torus Knot')
# show the label
a.legend()
# render the plot in the window
#plt.show()


#### 4 subplots

t1 = np.linspace(0,(2*1*pi)/4.,100)
t2 = np.linspace(0,(2*2*pi)/4.,100)
t3 = np.linspace(0,(2*3*pi)/4.,100)
t4 = np.linspace(0,(2*4*pi)/4.,100)
# First subplot
f1 = plt.figure()
s1=f1.add_subplot(221,projection='3d')
r1= 2+(4/5.)*cos(7*t1)
x1 = r*cos(4*t1)
y1 = r*sin(4*t1)
z1 = sin(7*t1)
s1.plot(x1,y1,z1)
print s1, str(s1)
# Second subplot
s2=f1.add_subplot(222,projection='3d')
r2= 2+(4/5.)*cos(7*t2)
x2 = r*cos(4*t2)
y2 = r*sin(4*t2)
z2 = sin(7*t2)
s2.plot(x2,y2,z2)
print s2, str(s2)

# Third subplot
s3=f1.add_subplot(223,projection='3d')
r3= 2+(4/5.)*cos(7*t3)
x3 = r*cos(4*t3)
y3 = r*sin(4*t3)
z3 = sin(7*t3)
s3.plot(x3,y3,z3)
print s3, str(s3)

# Third subplot
s4=f1.add_subplot(224,projection='3d')
r4= 2+(4/5.)*cos(7*t4)
x4 = r*cos(4*t4)
y4 = r*sin(4*t4)
z4 = sin(7*t4)
s4.plot(x4,y4,z4)
print s4, str(s4)



plt.show()

