# L-13 MCS 507 Wed 26 Sep 2012 : call_mpsolve.py

# Python wrapper around unisolve program of MPSolve-2.2.

from sympy import *

def mpsolve_integer_input(s):
   """
   Given in s is a string representing
   a polynomial in x with integer coefficients.
   On return is a string which can be
   written as an input file for unisolve.
   """
   x = var('x')
   p = eval(s)
   # print 'the expression p :', p
   q = Poly(p)
   L = q.all_coeffs()
   # print 'the list of coefficients :', L
   L.reverse()
   r = '! ' + s + '\n' + 'dri' + '\n'
   r = r + '0\n' + str(degree(q)) + '\n'
   for e in L: r = r + str(e) + '\n'
   return r

def random_number(n):
   """
   Returns a random number of n digits long.
   """
   import random
   r = random.randint(10**(n-1),10**n)
   return r

def write_input_file(s):
   """
   Generates a random file name and writes the
   string s to file.  Returns the name of the file.
   """
   name = 'in' + str(random_number(8))
   file = open(name,'w')
   file.write(s)
   file.close()
   return name

def get_unisolve_location():
   """
   Searches the command line for the location
   of the program, otherwise prompts the user.
   """
   import sys
   L = sys.argv
   if len(L) == 1: 
      prog = raw_input('give absolute path name for unisolve : ')
   else:
      prog = L[1]
   return prog

def extract_roots(name):
   """
   Give the name of the output file,
   returns the roots in a list.
   """
   f = open(name,'r')
   L = f.readlines()
   f.close()
   return [eval(e) for e in L]

def mpsolve(s,program='/tmp/unisolve'):
   """
   Given in the string s a polynomial in x,
   returns a list of roots.
   """
   input_data = mpsolve_integer_input(s)
   input_file = write_input_file(input_data)
   output_file = 'out' + str(random_number(8))
   cmd = program + ' ' + input_file + ' > ' + output_file
   import os
   os.system(cmd)
   R = extract_roots(output_file)
   os.remove(input_file)
   os.remove(output_file)
   return R

def main():
   """
   Prompts the user for a polynomial in x,
   and calls unisolve.
   """
   s = raw_input('give a polynomial in x : ')
   input_data = mpsolve_integer_input(s)
   unisolve = get_unisolve_location()
   # print 'writing', input_data
   input_file = write_input_file(input_data)
   output_file = 'out' + str(random_number(8))
   cmd = unisolve + ' ' + input_file + ' > ' + output_file
   print 'executing ' + cmd
   import os
   os.system(cmd)
   print 'the roots :', extract_roots(output_file)
   ans = raw_input('remove input and output files ? (y/n) ')
   if ans == 'y':
      os.remove(input_file)
      os.remove(output_file)

if __name__=='__main__': main()
