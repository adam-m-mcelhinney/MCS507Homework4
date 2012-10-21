"""
HW4, #1
L13, #3
Compute the roots of p = (x − c)**d + e in Sage for values of c
from 1 to 0, for increasing d and decreasing ǫ, makting sure the
working precision is high enough so 1.0 + e= 1.0. Relate the
location of the roots of p to values of c, d, and ǫ.

ASK PROF

"""
    

R = PolynomialRing(QQ, 'x,c')

p=(x-1)**1+0


for i in range(10):
    p=(x-c)*
