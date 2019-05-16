#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`Card` module

:author: `TEXIER Léane`_

:date: 2015, september

Cards are defined by a value and a color. 
Possible values and colors are listed in ``card.values`` and ``card.colors``.

"""

#import sys
import builtins
import random

    
## list of possible values and colors in ascending order
#values = ["7","8","9","10","Valet", "Dame ,"Roi", "As"]
values = ["7","8","9","10","Jack", "Queen" ,"King", "Ace"]
#colors = ["trefle", "carreau", "coeur", "pique"]
colors = ["club", "diamond", "heart", "spade"]


def create(value,color):
    """
    creates a card with value and color

    :param value: value of the card
    :type value: element of ``card.values``
    :param color: color of the card
    :type color: element of ``card.colors``
    :return: a new card with value  and color 
    :rtype: card
    :UC: value is in value and color is in colors
    """
    assert value in values," value must be one of"+str(values)
    assert color in colors," color must be one of"+str(colors)
    return {'value':value,'color':color}


def color(card):
    """
    returns the color of the card

    :param card: the card
    :param type: card
    :returns: *(element of ``card.colors``)* -- the color of the card
    :UC: none
    :Example:

    >>> c = create('Ace','heart')
    >>> color(c)
    'heart'
    """
    return card['color']

def value(card):
    """
    returns the value of the card

    :param card: the card
    :type card: card
    :returns: *(element of ``card.values``)* -- the value of the card
    :UC: none
    :Example:

    >>> c = create('Ace','heart')
    >>> value(c)
    'Ace'
    """
    return card['value']


def to_string(card):
    """
    returns a string representation of the card
    
    :param card: the card
    :type card: card
    :returns: *(string)* -- a string representation of the card
    :UC: none
    :Example:

    >>> c = create('Ace','heart')
    >>> to_string(c)
    'Ace of heart'
    """
    return card['value']+" of "+card['color']


def print(card, end='\n'):
    """
    print the card

    :param card: the card
    :type card: card
    :param end: [optional] separator (default is '\\\\n')
    :type end: string
    :UC: none
    
    """
    builtins.print(to_string(card))


def compare_value(card1, card2):
    """
    compares cards values, returns : 

    * a positive number if card1's value is greater than card2's
    * a negative number if card1's value is lower than card2's
    * 0 if card1's value is the same greater than card2's

    :param card1: the first card
    :type card1: card
    :param card2: the second card
    :type card2: card

    :returns: *(int)* --  
   
    * a positive number if card1's value is greater than card2's
    * a negative number if card1's value is lower than card2's
    * 0 if card1's value is the same greater than card2's

    :UC: none
    :Example: 

    >>> c1 = create('Ace','heart')
    >>> c2 = create('King','heart')
    >>> c3 = create('Ace','spade')
    >>> compare_value(c1,c2) > 0
    True
    >>> compare_value(c2,c1) < 0
    True
    >>> compare_value(c1,c3) == 0
    True
    """
    test=values.index(value(card1))-values.index(value(card2))
    if test>0:
        return 1
    elif test<0:
        return -1
    else:
        return 0


def compare_color(card1, card2):
    """
    compares cars colors, returns : 

    * a positive number if card1's color is greater than card2's
    * a negative number if card1's color is lower than card2's
    * 0 if card1's color is the same greater than card2's

    :param card1: the first card
    :type card1: card
    :param card2: the second card
    :type card2: card
    :returns: *(int)* --
  
    * a positive number if card1's color is greater than card2's
    * a negative number if card1's color is lower than card2's
    * 0 if card1's color is the same greater than card2's

    :UC: none
    :Example: 

    >>> c1 = create('Ace','heart')
    >>> c2 = create('King','heart')
    >>> c3 = create('Ace','spade')
    >>> compare_color(c1,c3) < 0
    True
    >>> compare_color(c3,c1) > 0
    True
    >>> compare_color(c1,c2) == 0
    True
    """
    test=colors.index(color(card1))-colors.index(color(card2))
    if test>0:
        return 1
    elif test<0:
        return -1
    else:
        return 0


def compare(card1,card2):
    """
    compares cards, first it compares cards values and if equal cards colors returns : 

    * a positive number if card1 is greater than card2
    * a negative number if card1 is lower than card2
    * 0 if card1 is the same greater than card2

    :param card1: the first card
    :type card1: card
    :param card2: the second card
    :type card2: card

    :returns: *(int)* --
     
    * a positive number if card1 is greater than card2
    * a negative number if card1 is lower than card2
    * 0 if card1 is the same greater than card2

    :UC: none
    :Example: 

    >>> c1 = create('Ace','heart')
    >>> c2 = create('King','heart')
    >>> c3 = create('Ace','spade')
    >>> c1bis = create('Ace','heart')
    >>> compare(c1,c2) > 0
    True
    >>> compare(c2,c1) < 0
    True
    >>> compare(c1,c3) < 0
    True
    >>> compare(c1,c1bis) == 0
    True
    """
    if compare_value(card1,card2)==0:
        return compare_color(card1,card2)
    return compare_value(card1,card2)


def random_card():
    """
    create a cards whose value and color are randomly chosen

    :returns: *(card)* -- a randomly chosen card
    """
    value_idx=random.randint(len(values)-1)
    color_idx=random.randrange(len(colors))
    return create(values[value_idx],colors[color_idx])

if __name__ == '__main__':
    import doctest
    doctest.testmod ()    
