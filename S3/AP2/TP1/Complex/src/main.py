#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
	A little program using complex module. Type ``usage()``.
	
	Change ``complex2`` with ``complex1`` in ``import complex2 with cplx`` to test the implementation with dictionnary.
"""


import sys

import complex1 as cplx

def usage ():
    print ('Usage : {:s} x1 x2 x3 x4'.format(sys.argv[0]))
    print ('with x1, x2, x3, x4 real numbers')
    exit (1)
    
if len (sys.argv) != 5:
    usage ()
    
z1 = cplx.create (float (sys.argv[1]), float (sys.argv[2]))
z2 = cplx.create (float (sys.argv[3]), float (sys.argv[4]))

print ('z1 = ',end='')
cplx.print (z1)
print ("z1's modulus = {:f}".format (cplx.modulus (z1)))
print()

print ('z2 = ',end='')
cplx.print (z2)
print ("z2's modulus = {:f}".format (cplx.modulus (z2)))
print()

print ('z1 + z2 = ',end='')
cplx.print (cplx.add(z1,z2))
print()

# eof
