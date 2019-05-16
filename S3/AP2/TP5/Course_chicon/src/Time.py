#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`time` module

:author: FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>_

:date: October, 2015

Module for time representation.



"""

class InvalidTimeError (Exception):
    """
    """
    def __init__ (self, msg):
        self.message = msg
        
def create (h,m,s):
    """
    
    :param h: number of hours
    :type h: int
    :param m: number of minutes
    :type m: int
    :param s: number of seconds
    :type s: int
    :return: a duration 
    :rtype: time
    :UC: 0 <= h, 0 <= m,s < 60
    """
    if (h < 0 or m < 0 or m > 59 or
        s < 0 or s > 59):
        raise InvalidTimeError ('bad data for a duration : {:d},{:d},{:d}'.format(h,m,s))
    else:
        return (h,m,s)

def get_hours (d):
    """
    
    :param d:
    :type d: time
    :return: number of hours of duration d
    :rtype: int
    :UC: none
    """
    return d[0]

def get_minutes (d):
    """
    
    :param d:
    :type d: time
    :return: number of minutes of duration d
    :rtype: int
    :UC: none
    """
    return d[1]

def get_secondes (d):
    """
    
    :param d:
    :type d: time
    :return: number of secondes of duration d
    :rtype: int
    :UC: none
    """
    return d[2]


def compare (d1,d2):
    """
    
    :param d1:
    :type d1: time
    :param d2:
    :type d2: time
    :return: - -1 if duration d1 is shorter than  duration d2
             - 1 if duration d1 is longer than  duration d2
             - 0 otherwise
    :rtype: int
    :UC: none
    """
    delta = (get_hours (d1) - get_hours (d2),
             get_minutes (d1) - get_minutes(d2),
             get_secondes (d1) - get_secondes (d2))
    if delta[0] < 0:
        return -1
    elif delta[0] > 0:
        return 1
    elif delta[1] < 0:
        return -1
    elif delta[1] > 0:
        return 1
    elif delta[2] < 0:
        return -1
    elif delta[2] > 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    pass    


