# -*- coding: utf-8 -*-

"""
:mod:`test` module : test module for experiences assignment

:author: Léane TEXIER & Antonio Viana SIMONE JUNIOR 

:date: 2015, december
"""

import sys
import experience
import sorting

def compare (m1,m2):
    ##global cpt
    ##cpt+=1
    return experience.compare(m1,m2)


# STRATEGY 1
def negative_markers1(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.

    :param m: The list of markers
    :type m: List of String
    :param p: The list of positive markers
    :type m: List of String
    :return: The list of negative markers
    :rtype: List of String
    """
    negative = []
    global cpt
    for m in markers:
        found = False
        i=0
        while i < len(positive) and not found:
            if compare(m,positive[i])==0:
                found=True
            i+=1
        if not found:
            negative.append(m)
    return negative


# STRATEGY 2
def negative_markers2(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of (sorted) positive markers.

    :param m: The list of markers
    :type m: List of String
    :param p: The list of positive markers
    :type m: List of String
    :return: The list of negative markers
    :rtype: List of String
    """
    negative = []
    p=sorting.merge_sort(positive,compare)
    #global cpt
    if len(markers)==len(p):
        return negative
    for m in markers:
        inf = 0
        sup = len(p)
        while sup-inf>1:
            mil = (sup + inf)//2
            comp = compare(m,p[mil])
            if comp == -1:
                sup = mil
            elif comp == 1:
                inf = mil
            else:
                break
        comp2 =compare(p[(sup + inf)//2],m)
        if comp2!=0:
            negative.append(m)        
    return negative


# STRATEGY 3
def negative_markers3(markers,positive):
    """
    Computes the list of negative markers from the list of (sorted) markers and
    the list of (sorted) positive markers.

    :param m: The list of markers
    :type m: List of String
    :param p: The list of positive markers
    :type m: List of String
    :return: The list of negative markers
    :rtype: List of String
    """
    negative = []
    global cpt
    m=sorting.merge_sort(markers,compare)
    p=sorting.merge_sort(positive,compare)
    while len(p)!=0:
        comp = compare(m[0],p[0])
        if comp==0:
            p=p[1:]
            m=m[1:]
        elif comp==1:
            p=p[1:]
        else:
            negative.append(m[0])
            m=m[1:]
    negative.extend(m)
    return negative

        
if __name__ == "__main__":
    m = int(sys.argv[1])   
    for i in range(1,m+1):
        p=i
        markers = experience.markers(m)
        positive = experience.experience(p,markers)
        print("%d %d"%(m,p),end="")
        cpt = 0
        negative_markers1(markers,positive)
        print(" %d" % (cpt), end="")
        cpt = 0
        negative_markers2(markers,positive)
        print(" %d" % (cpt), end="")
        cpt = 0
        negative_markers3(markers,positive)
        print(" %d" % (cpt))
