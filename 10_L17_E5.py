"""
HW4, #10
L17, #5

Experiment with the number of samples for z and the speed of the
movie. Does the movie run twice as fast if we cut the number of
samples in half? Does the cutting of samples reduce the accuracy
of the plot?

"""


# L-17 MCS 507 Fri 5 Oct 2012 : heatmovie

# The script makes an animation of a model of a heat wave.

from scitools.std import *
from datetime import datetime

def animate(tmax,dt,x,function,ymin,ymax,t0=0,
            xlabel='x',ylabel='y',file='C:/Users/Adam2/Documents/GitHub/MCS507Homework4/'):
   """
   Makes plots for t from t0 to tmax with steps dt,
   evaluating the function.
   """
   t = t0; counter = 0
   while (t <= tmax):
      y = function(x,t)
      plot(x,y,
           axis=[x[0],x[-1],ymin,ymax],
           title = 'time=%2d h'%(t/3600.0),
           xlabel=xlabel,ylabel=ylabel,
           savefig=file + '%04d.png' % counter)
      t = t + dt; counter = counter + 1
     
# global variables of the model

k = 1.E-6      # thermal diffusivity
P = 24*3600    # oscillation period in seconds
omega = 2*pi/P
dt = P/24      # time lag is one hour
#tmax = 3*P     # 3 day and night simulation
tmax = P     # 3 day and night simulation
T0 = 10        # mean temperature in Celsius
A = 10         # max amplitude variation
a = sqrt(omega/(2*k))
D = -(1/a)*log(0.001) # maximal depth
n = 501        # number of points in z-direction

def T(z,t):
   """
   Evaluates our mathematical model.
   """
   return T0 + A*exp(-a*z)*cos(omega*t - a*z)


"""
Calls the animate command to make a movie.
"""
start=datetime.now()
z = linspace(0,D,n)
while True:
   animate(tmax,dt,z,T,T0-A,T0+A,0,'z','T')
   #ans = raw_input('play it again? (y/n) '
   ans='n'
   if ans != 'y': break
end=datetime.now()
print end-start
# time: 0:00:35.034000

start=datetime.now()
z = linspace(0,D,n/2.)
while True:
   animate(tmax,dt,z,T,T0-A,T0+A,0,'z','T')
   #ans = raw_input('play it again? (y/n) '
   ans='n'
   if ans != 'y': break
end=datetime.now()
print end-start
# time: 0:00:33.997000

start=datetime.now()
z = linspace(0,D,n/10.)
while True:
   animate(tmax,dt,z,T,T0-A,T0+A,0,'z','T')
   #ans = raw_input('play it again? (y/n) '
   ans='n'
   if ans != 'y': break
end=datetime.now()
print end-start
# 0:00:33.984000


