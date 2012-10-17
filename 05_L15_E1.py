"""
HW4, #5
L15, #1
The animation of the sine with increasing frequency produced
plots which became less smooth as the frequency increased.
Modify the making of the movie with a proper adjustment of the
step size used for sampling. Justify your choice of the step size.

"""

# We plot sin functions of increasing frequencies.

from scitools.std import *
x = arange(0,2*pi,0.01)
#figure()
#axis([0,2*pi,-1.5,+1.5])
for i in xrange(1,11):
   #x = arange(0,1,0.01)
   # Need to decrease step size as frequency increases to keep the number of points per 2*pi cylce the same
   x = arange(0,1,0.01/i)
   print len(x)
   y = sin(i*2*pi*x)
   plot(x,y,axis=[0,1,-1.5,+1.5],
        legend='frequency = %d' % i,
        savefig='mov%02d.png' % i)
movie('mov*.png')
