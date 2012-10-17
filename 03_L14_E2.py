"""
HW4, #3
L14, #2

Evaluate x**2 + 2x − 1 = (x + 2)x − 1 at a, where a =
numpy.linspace(0,1,1000) with inplace arithmetic defined
by y = a; y += 2; y *= a; y -= 1.
Wrap the inplace arithmetic sequence for x2 + 2x − 1 in a function
and compare the execution time to the vectorized version of
(x + 2)x − 1.


ASK PROF IF THIS IS RIGHT. SEEMS ODD

"""

from numpy import linspace

    
f=lambda x: x**2+2*x-1
a=linspace(0,1,1000)


def inplace(f,a,n):
    """
    Computes the inplace arithmetic and outputs time
    """
    from datetime import datetime
    #import timeit
    start=datetime.now()
    #t=timeit.timeit(f(a),number=1000)
    for i in range(n):
        f(a)
        
    end=datetime.now()
    return end-start,end,start
    #return t

n=10000
t=inplace(f,a,n)
print t[0]
# time:
# (datetime.timedelta(0, 0, 500000)


from numpy import vectorize
from datetime import datetime

g=lambda x: (x+2)*x-1
vg=vectorize(g)
start=datetime.now()
for i in range(n):
    vg(a)
end=datetime.now()
print end-start

# time
# 0:00:08.406000


