#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`competitor` module

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: October, 2015

Module for competitor representation.
A competitor

"""

def create (first_name, last_name, sex, num):
    """
    
    :param first_name: first name of a competitor
    :type name: string
    :param last_name: last name of a competitor
    :type name: string
    :param sex: sex of a competitor 'M' or 'F'
    :type name: string
    :param num: bib number of the competitor
    :type num: int
    :return: a new record for this competitor
    :rtype: competitor
    :UC: num > 0 and sex in 'MF'
    """
    assert type (num) == type (0) and num > 0
    ##assert sex in 'MF'
    return {
        'first_name' : first_name,
        'last_name' : last_name,
        'sex' : sex,
        'num' : num,
        'performance' : None
    }

def get_firstname (comp):
    """
    
    :param comp:
    :type comp: competitor
    :return: first name of competitor comp
    :rtype: str
    :UC: none
    """
    return comp['first_name']

def get_lastname (comp):
    """
    
    :param comp:
    :type comp: competitor
    :return: last name of competitor comp
    :rtype: str
    :UC: none
    """
    return comp['last_name']

def get_bibnum (comp):
    """

    :param comp:
    :type comp: competitor
    :return: bib number of competitor comp
    :rtype: str
    :UC: none

    """
    return comp['num']

def get_performance (comp):
    """

    :param comp:
    :type comp: competitor
    :return: performance of competitor comp
    :rtype: time
    :UC: none
    """
    return comp['performance']


def get_sex (comp):
    """

    :param comp:
    :type comp: competitor
    :return: sex of competitor comp
    :rtype: time
    :UC: none
    """
    return comp['sex']

def set_perf (comp, d):
    """

    :param comp: competitor to be modified
    :type comp: competitor
    :param d: performance of competitor comp
    :type d: time
    :return: None
    :Side effect: performance of competitor comp is modified with value d
    :UC: none
    """
    comp['performance'] = d

    
    
if __name__ == '__main__':
    pass    


