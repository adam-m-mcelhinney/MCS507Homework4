"""
HW4, #1
L13, #3
Compute the roots of p = (x − c)**d + e in Sage for values of c
from 1 to 0, for increasing d and decreasing ǫ, makting sure the
working precision is high enough so 1.0 + e= 1.0. Relate the
location of the roots of p to values of c, d, and ǫ.

ASK PROF

Per Prof, see how location of roots changes as c,d,and e change

"""
    


n=10;d=1;e=1

for i in range(10):
    c=1-i*(1./10)
    print c
    p=(x-c)**d+e
    p.roots(ring=ComplexField(100))


d=5
e=.5
for i in range(10):
    c=1-i*(1./10)
    print c
    p=(x-c)**d+e
    p.roots(ring=ComplexField(100))

d=10
e=.25
for i in range(10):
    c=1-i*(1./10)
    print c
    p=(x-c)**d+e
    p.roots(ring=ComplexField(100))
