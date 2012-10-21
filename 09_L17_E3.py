"""
HW4, #9
L17, #3

Use Sage or sympy to show that its solution
k1 sin(z√−Iω) + k2 cos(z√−Iω) is mathematically equivalent to
Y(z) = c1*e**(z√iω) + c2*e**(−z√iω)

Done

"""


from sympy import *

#f= lambda z: k1*sin(z*sqrt(-i*w))+k2*cos(z*sqrt(-i*w))
k1,k2,z,w,c1,c2,r=symbols('k1,k2,z,w,c1,c2,r')

g=k1*sin(z*sqrt(-I*w))+k2*cos(z*sqrt(-I*w))
t=g.expand(basic=True)

# Recall
#sinh(z)=(exp(2*z)-1)/(2.*exp(z))
#cosh(z)=(exp(2*z)+1)/(2.*exp(z))
r=(-1)**(1/4)*w**(1/2)*z
q=I*k1*(exp(2*r)-1)/(2.*exp(r))+k2*(exp(2*r)+1)/(2.*exp(r))
q.expand()


f=c1*exp((z*sqrt(I*w)))+c2*exp((-z*sqrt(I*w)))

