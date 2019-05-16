#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`complex1` module : version 1 of a (simple) module for complex numbers

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2015, september

Complex numbers are represented with dictionaries 

.. seealso::
           :mod:`complex2`
"""

import builtins, math

def create (x,y):
    """
    create a complex number with real part x and imaginary part y

    :param x: the real part of the complex number to create
    :type x: int or float
    :param y: the imaginary part of the complex number to create
    :type y: int or float
    :return: the complex number x + iy
    :rtype: complex
    :UC: none
    :Example:

    >>> z = create (1,2)
    >>> real_part (z)
    1
    >>> imag_part (z)
    2
    """
    assert type(x) in {int,float}, 'first argument is not int or float' 
    assert type(y) in {int,float}, 'second argument is not int or float' 
    return {'re' : x, 'im' : y}

def from_real_number (x):
    """
    create the complex number x + i0 from real number x

    :param x: a real number
    :type x: int or float
    :return: the complex number x + 0i
    :rtype: complex
    :UC: none
    :Example:

    >>> z = from_real_number (1)
    >>> real_part (z)
    1
    >>> imag_part (z)
    0
    """
    return create (x,0)


def real_part (z):
    """
    return the real part of complex number z

    :param z: a complex number
    :type z: complex
    :return: the real part of z
    :rtype: int or float
    :UC: none
    :Example:

    >>> z = create (1,2)
    >>> real_part(z)
    1
    """
    return z['re']

def imag_part (z):
    """
    return the imaginary part of complex number z

    :param z: a complex number
    :type z: complex
    :return: the imaginary part of z
    :rtype: int or float
    :UC: none
    :Example:

    >>> z = create (1,2)
    >>> imag_part(z)
    2
    """
    return z['im']

def equal (z1, z2):
    """
    return True if complex numbers z1 and z2 are equals
           False otherwise

    :param z1: a complex number
    :type z1: complex
    :param z2: a complex number
    :type z2: complex
    :return: True if z1 = z2, False otherwise
    :rtype: bool
    :UC: none
    :Example:

    >>> z1 = create (1,2)
    >>> z2 = create (1,2)
    >>> z3 = create (1,-1)
    >>> equal (z1,z2)
    True
    >>> equal (z1,z3)
    False
    """
    return real_part (z1) == real_part (z2) and imag_part (z1) == imag_part (z2) 

def modulus (z):
    """
    return the modulus of complex number z, ie :math:`\sqrt{x^2 + y^2}` 
    if $z=x+yi$

    :param z: a complex number
    :type z: complex
    :return: his modulus
    :rtype: float
    :UC: none
    :Example:

    >>> modulus (create (0,0))
    0.0
    >>> modulus (create (3,4))
    5.0
    """
    x = real_part (z)
    y = imag_part (z)
    return math.sqrt (x**2 + y**2)

def add (z1,z2):
    """
    return the sum of the two complex numbers z1 and z2
    
    :param z1: a complex number
    :type z1: complex
    :param z2: a complex number
    :type z2: complex
    :return: z1 + z2
    :rtype: complex
    :UC: none
    :Example:

    >>> z = add (create (1,2), create (3,4))
    >>> real_part (z)
    4
    >>> imag_part (z)
    6
    """
    x1 = real_part (z1)
    x2 = real_part (z2)
    y1 = imag_part (z1)
    y2 = imag_part (z2)
    return create (x1 + x2, y1 + y2)

def mult (z1,z2):
    """
    return the product of the two complex numbers z1 and z2
    
    :param z1: a complex number
    :type z1: complex
    :param z2: a complex number
    :type z2: complex
    :return: z1 * z2
    :rtype: complex
    :UC: none
    :Example:

    >>> z = mult (create (1,2), create (3,4))
    >>> real_part (z)
    -5
    >>> imag_part (z)
    10
    
    """
    x1 = real_part (z1)
    x2 = real_part (z2)
    y1 = imag_part (z1)
    y2 = imag_part (z2)
    return create (x1*x2 - y1*y2, x1*y2 + y1*x2)
    

def __to_string (z):
    """
    return a string representation of the complex number z with algebraic form
    `x+yi` where x = real part of z and y = imaginary part

    :param z: complex number to convert
    :type z: complex
    :return: a string representation of z
    :rtype: string
    :UC: none
    """
    return '{:f} + {:f}i'.format(real_part(z),imag_part(z))

def print (z, end='\n'):
    """
    print the complex number z with algebraic form `x + yi`
    where x = real part of z and y = imaginary part

    :param z: complex number to print
    :type z: complex
    :param end: [optional] separator (default is '\\\\n')
    :type end: string
    :return: None
    :UC: none
    """
    builtins.print (__to_string (z))

if __name__ == '__main__':
    import doctest
    doctest.testmod ()

# eof
