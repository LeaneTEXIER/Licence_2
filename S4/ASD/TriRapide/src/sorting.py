# -*- coding: utf-8 -*-

"""
:mod:`sorting` module : sorting functions module for quicksort assignment

:author: Léane TEXIER & Antonio Viana SIMONE JUNIOR 

:date: 2016, january
"""

import copy
import test
import generate
import random


def merge (t1,t2, cmp):
    """
    Given two sorted list, creates a fresh sorted list.
    
    :param t1: A list of objects
    :type t1: list
    :param t2: A list of objects
    :type t1: list
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A fresh list, sorted.
    :rtype: list
    
    .. note::
    
       time complexity of merge is :math:`O(n_1+n_2)` with
       :math:`n_1` and :math:`n_2` resp. the length of *t1* and *t2*

    """
    n1 = len(t1)
    n2 = len(t2)
    t = [ 0 for i in range(0,n1+n2)]
    i = j = k = 0
    while i < n1 and j < n2:
        if cmp(t1[i],t2[j]) < 0:
            t[k] = t1[i]
            i = i + 1
        else:
            t[k] = t2[j]
            j = j + 1
        k = k + 1
    while i < n1:
        t[k] = t1[i]
        i = i + 1
        k = k + 1
    while j < n2:
        t[k] = t2[j]
        j = j + 1
        k = k + 1
    return t


def merge_sort (t,cmp):
    """
    A sorting function implementing the merge sort algorithm
    
    :param t: A list of integers
    :type t: list
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A fresh list, sorted.
    :rtype: list
    """
    n = len(t)
    if n <= 1:
        # cas de base
        return copy.deepcopy(t)
    else:
        # cas general
        t1 = merge_sort((t[0:((n-1)//2+1)]),cmp)
        t2 = merge_sort((t[((n-1)//2+1):n]),cmp)
        return merge(t1,t2,cmp)
    

def quicksort (t,cmp, pivotalea=False):
    """
    A sorting function implementing the quicksort algorithm
    
    :param t: A list of integers
    :type t: list
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: Nothing
    .. note::
       *t* is modified during the sort process
    """
    quicksort_slice({'data':t, 'left':0, 'right':len(t)-1}, cmp, pivotalea=pivotalea)


def quicksort_slice (s, cmp, pivotalea=False):
    """
    A sorting function implementing the quicksort algorithm
    
    :param s: A slice of a list, that is a dictionary with 3 fields :
              data, left, right representing resp. a list of ibjects and left
              and right bounds of the slice.
    :type s: dict
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: Nothing
    """
    right=s['right']
    left=s['left']
    if right>left:
        s1,s2 = partition(s,cmp, pivotalea=pivotalea)
        s2['left']+=1
        quicksort_slice(s1,cmp, pivotalea=pivotalea)
        quicksort_slice(s2,cmp, pivotalea=pivotalea)

    
def partition (s, cmp, pivotalea=False):
    """
    Creates two slices from *s* by selecting in the first slice all
    elements being less than the pivot and in the second one all other
    elements.

    :param s: A slice of a list, that is a dictionary with 3 fields :
              data, left, right representing resp. a list of ibjects and left
              and right bounds of the slice.
    :type s: dict
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A couple of slices, the pivot being at the left index of the second slice.
    :rtype: tuple
    """
    global cpt
    l=s['data']
    left=s['left']
    right=s['right']
    if pivotalea:
        pos_pivot=random_pivot(s)
        l[left],l[pos_pivot]=l[pos_pivot],l[left]
    pos_pivot=left
    pivot=l[pos_pivot]
    left+=1
    while left<=right:
        if cmp(l[left],l[pos_pivot])==-1:
            l[left],l[pos_pivot]=l[pos_pivot],l[left]
            pos_pivot+=1
            left+=1
        else:
            l[left],l[right]=l[right],l[left]
            right-=1
    s1={'data' : l, 'left' : s['left'], 'right': pos_pivot - 1}
    s2={'data' : l, 'left' : pos_pivot, 'right': s['right']}
    return (s1,s2)


def random_pivot(s):
    i = random.randint(s['left'],s['right'])
    return i


