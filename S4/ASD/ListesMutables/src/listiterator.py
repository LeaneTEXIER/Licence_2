# -*- coding: utf-8 -*-

""":mod:`listiterator` module : list implementation with iterator interaction

Provides constructor, selectors and modifiers for mutable lists.
Lists of this module must be traversed via iterators. 

An iterator for lists allows the programmer to traverse the list in
either direction and adding elements to the list during iteration.  

An iterator has no current element; its cursor position always lies
between the element that would be returned by a call to :code:`previous` and
the element that would be returned by a call to `next`. 

An iterator for a list of length n has n+1 possible cursor positions,
as illustrated by the carets (^) below:

.. code::
                      Element(0)   Element(1)   Element(2)   ... Element(n-1)
 cursor positions:  ^            ^            ^            ^                  ^

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2016, january

"""

class EmptyList (Exception):
    """
    Exception for empty lists
    """
    def __init__ (self,msg):
        self.message = msg

class NoSuchElementException (Exception):
    """
    Exception for iterators not positionned
    """
    def __init__ (self,msg):
        self.message = msg
        
def __new_cell (v,next_cell,prev_cell):
    return { "value" : v, "next" : next_cell, "prev" : prev_cell }

def __empty_cell (c):
    return c == None

def empty_list ():
    """
    Creates a new empty list.

    :return: A frest list
    :rtype: dict
    """    
    return { "head" : None, "tail" : None }

def is_empty (l):
    """
    Returns true if the list is empty, false else.
    
    :param l: The list
    :type l: dict
    :rtype: boolean
    """
    return l == { "head" : None, "tail" : None }

def cons (l,v):
    """
    Add the value :code:`v` at the begining of the list :code:`l`.

    :param l: The list, possibly empty.
    :type l: dict
    :param v: The value to be added.
    :type v: Any

    UC: not compatible once iterators have been used
    """
    if l["head"] == None:
        l["head"] = l["tail"] = __new_cell (v, None, None)
    else:
        l["head"] = __new_cell (v, l["head"], None)
        l["head"]["next"]["prev"] = l["head"]

def __print_without_iterator (c):
    """
    :param c: A cell
    :type c: dict
    """
    if __empty_cell(c):
        print()
    else:
        print(c["value"],end=' ')
        __print_without_iterator (c["next"])

def __print_without_iterator_reversed (c):
    """
    :param c: A cell
    :type c: dict
    """
    a=c['prev']
    print(c['value'],end=' ')
    while a!= None:
        print(a['value'],end=' ')
        a=a['prev']

def print_list (l,reverse=False):
    if is_empty(l):
        raise Empty_List("The list has no elements")
    if reverse:
        __print_without_iterator_reversed (l["tail"])
    else:
        __print_without_iterator (l["head"])


def get_listiterator (l, from_the_end = False):
    """
    Creates a newiterator for list *l*.

    :param l: The list
    :type l: dict
    :return: An iterator at the begining of the list
    :rtype: dict
    """
    if from_the_end:
        end=l['tail']
        while end['next']!=None:
            end=end['next']
        return {'prev': end, 'next': None}
    else:
        begin=l['head']
        if begin!=None :
            while begin['prev']!=None:
                begin=begin['prev']
        else:
            begin=None     
        return {'prev': None, 'next': begin}

def hasNext (it):
    """
    Returns :code:`True` if this list iterator has more elements when
    traversing the list in the forward direction. (In other words,
    returns :code:`True` if :code:`next(it)` would return an element rather than
    throwing an exception.)

    :param it: The iterator
    :type it: dict
    :rtype: boolean
    """
    return (not it["next"]==None)

def next (it):
    """
    Returns the next element in the list and advances the cursor
    position. This method may be called repeatedly to iterate through
    the list, or intermixed with calls to :code:`previous(it)` to go back and
    forth. (Note that alternating calls to next and previous will
    return the same element repeatedly.)

    :param it: The iterator
    :type it: dict
    """
    if hasNext(it):
        nextt=it['next']
        it['prev']=nextt
        it['next']=nextt['next']
        return (nextt['value'])
    else:
        raise NoSuchElementException("No next element")

def hasPrevious (it):
    """
    Returns :code:`True` if this list iterator has more elements when
    traversing the list in the reverse direction. (In other words,
    returns :code:`True` if :code:`previous(it)` would return an
    element rather than throwing an exception.)

    :param it: The iterator
    :type it: dict
    :rtype: boolean
    """
    return (not it["prev"]==None)

def previous (it):
    """
    Returns the previous element in the list and moves the cursor
    position backwards. This method may be called repeatedly to
    iterate through the list backwards, or intermixed with calls to
    :code:`next(it)` to go back and forth. (Note that alternating calls to next
    and previous will return the same element repeatedly.)

    :param it: The iterator
    :type it: dict
    """
    if hasPrevious(it):
        prevv=it['prev']
        it['prev']=prevv['prev']
        it['next']=prevv
        return (prevv['value'])
    else:
        raise NoSuchElementException("No previous element")

def add (it,v):
    """Inserts the specified element into the list. The element is
    inserted immediately before the element that would be returned by
    next(), if any, and after the element that would be returned by
    previous(), if any. (If the list contains no elements, the new
    element becomes the sole element on the list.) The new element is
    inserted before the implicit cursor: a subsequent call to next
    would be unaffected, and a subsequent call to previous would
    return the new element.

    :param it: The iterator
    :type it: dict
    :param v: The element
    :type v: Any
    """
    vv=__new_cell (v,None,None)
    if hasPrevious(it):
        p=it['prev']
        if hasNext(it):
            n=it['next']
            p['next']=vv
            n['prev']=vv
            vv['prev']=p
            vv['next']=n
            next(it)
            previous(it)
        else:
            p['next']=vv
            vv['prev']=p
            it['next']=vv
            next(it)
    else:
        if hasNext(it):
            n=it['next']
            vv['next']=n
            n['prev']=vv
            next(it)
            previous(it)
        else:
            it['prev']=vv
            vv['next']=it['prev']
            print("vv",vv)       
            
            
            
    
    
