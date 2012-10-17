# L-10 MCS 507 Wed 19 Sep 2012 : newtoniterator.py

# Adding a callback function to a Newton function
# we can see intermediate results and even stop the iteration,
# but the callback function remains subordinate to the main
# function that performs the Newton iterations.

# The class NewtonIterator defines an object that stores
# the state of all variables in a Newton iteration.

# This file defines a class Counter.
# An object of this class can be used as a counter.
# We use this as a template to invert the control
# of the function Newton.

# We can use the code in this file as a module
# and import the class definition in an interactive session
# or into another Python program.
# Because of the last line, we can also run this file
# as $ python counter.py and execute the test program.

class NewtonIterator():
   """
   A Newton iterator applies the Newton operator
   to find a solution to the equation f(x) = 0.
   """
   def __init__(self,f,df,x0,n=5,eps=1.0e-8):
      """
      Initializes the state of the iterator.
      """
      self.step = 0
      self.f = f
      self.df = df
      self.x = float(x0)
      self.max = n
      self.eps = eps
      self.dx = 1.0
      self.res = abs(f(x0))

   def __str__(self):
      """
      Returns the string representation
      of the data attributes.
      """
      s = "step %d : " % self.step
      s = s + ("x = %.16e" % self.x)
      s = s + (", |dx| = %.3e" % self.dx)
      s = s + (", |f(x)| = %.3e" % self.res)
      return s

   def __repr__(self):
      """
      Defines the representation. 
      """
      return self.__str__()
  
   def next(self):
      """
      Does one Newton step.
      """
      self.step = self.step + 1
      if (self.step > self.max):
         raise StopIteration("only %d steps allowed" % self.max)
      else:
         z = self.x
         self.dx = -self.f(z)/self.df(z)
         self.x = z + self.dx
         self.dx = abs(self.dx)
         self.res = abs(self.f(self.x))

   def accurate(self):
      """
      Returns True if the accuracy requirements
      are satisfied.  Returns False otherwise.
      """
      return ((self.dx <= self.eps) or
              (self.res <= self.eps))

def test():
   """
   Approximates the square root of 2.
   """
   f = lambda x: x**2 - 2.0
   df = lambda x: 2.0*x
   nf = NewtonIterator(f,df,2.0)
   print nf
   for i in xrange(5):
      nf.next()
      print nf
      if nf.accurate(): break

if __name__=="__main__": test()
