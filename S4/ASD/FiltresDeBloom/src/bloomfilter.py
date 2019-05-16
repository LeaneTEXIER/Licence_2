# -*- coding: utf-8 -*-

""":mod:`bloomfilter` module : Implements a bloomfilter.

:author: Léane TEXIER & Antonio Viana SIMONE JUNIOR & `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2016, january

"""

def create (n,f,m):
    """
    Creates a new empty Bloom filter of size :math:`2^n`

    :param n: the log of the size of the filter
    :type n: int
    :param f: the hash function whose should take as input two 
              parameters: the value to be hashed and the number 
              of the subfunction used
    :type f: function(any,int)
    :param m: the number of functions provided by *f*
    :return: the new Bloom filter
    :rtype: dict
    """
    return {"lenght":2**n, "nb_function":m, "function":f, "tab":{i:False for i in range (2**n)}}

def add (bf, e):
    """
    Adds *e* to *bf*.

    :param bf: A Bloom filter
    :type bf: dict
    :param e: The element to be added
    :type e: Any
    """
    f_hash=bf['function']
    m=bf['nb_function']
    for i in range(1,m+1):
        val=f_hash(e,i)%bf['lenght']
        bf["tab"][val]=True
    
def contains (bf, e):
    """
    Returns True if *e* is in *bf*.

    :param bf: A Bloom filter
    :type bf: dict
    :param e: The element to be tested
    :type e: Any
    """
    f_hash=bf['function']
    m=bf['nb_function']
    for i in range(1,m+1):
        val=f_hash(e,i)%bf['lenght']
        if bf["tab"][val]==False:
            return False
    return True
