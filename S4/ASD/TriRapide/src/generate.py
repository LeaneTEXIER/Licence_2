# -*- coding: utf-8 -*-

"""
:mod:`generate` module : list facilities module for quicksort assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2016, january
"""

import random

def is_sorted(t):
    """
    Predicate to test whether a list is sorted in increasing order.

    :param t: A list of integers
    :type t: list
    
    :return: True if the list is sorted, else False
    :rtype: bool
    
    >>> is_sorted([1,2,3])
    True
    >>> is_sorted([1,3,2])
    False
    """
    n = len(t)
    i = 0
    while i < n-1 and t[i] <= t[i+1]:
        i = i + 1
    return i == n - 1

def decreasing_list(n):
    """
    Creates a fresh list with integers in decreasing order.
    
    :param n: The length of the list
    :type t: int
    
    :return: A list of int from n-1 to 0
    :rtype: list
    
    >>> decreasing_list(3)
    [2,1,0]
    """
    return [i for i in range(n)]

def increasing_list(n):
    """
    Creates a fresh list with integers in increasing order.
    
    :param n: The length of the list
    :type t: int
    
    :return: A list of int from 0 to n-1
    :rtype: list
    
    >>> increasing_list(3)
    [0,1,2]
    """
    return [i for i in reversed(range(n))]


def random_list(n):
    """
    Creates a fresh list with integers in random order. Each int from
    0 to n-1 is present only once.
    
    :param n: The length of the list
    :type t: int
    
    :return: A list of int from 0 to n-1
    :rtype: list
    
    >>> random_list(3)
    [0,1,2]
    >>> random_list(3)
    [1,0,2]
    
    """
    l = increasing_list(n)
    random.shuffle(l)
    return l
