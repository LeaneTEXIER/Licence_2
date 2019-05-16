
# -*- coding: utf-8 -*-

"""
TP AP2 PROJET
Licence 2 de mathématiques
Univ. Lille 1

points.py

Module de selecteurs ( coordonnées du mileu du cercle et son rayon ) 

"""

__author__ = 'DEBRAY Julie, FONTAINE Mallaury, TEXIER Léane'
__date_creation__ = 'novembre 2015'


### Import des modules ###
from tkinter import *
from math import *

### Sélecteurs ###
    
def get_x(cercle):
    """
    renvoie la coordonnee x du cercle passe en parametre

    :param cercle: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle et le rayon
    :type cercle: tuple
    :return: la coordonnee x du centre du cercle
    :rtype: float
    :UC: type(x)==type(y)==type(rayon)==float

    :Example:
    >>> get_x((230,230,10))
    230
    
    """
    return cercle[0]

def get_y(cercle):
    """
    renvoie la coordonnee y du cercle passe en parametre

    :param cercle: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle et le rayon
    :type cercle: tuple
    :return: la coordonnee y du centre du cercle
    :rtype: float
    :UC: type(x)==type(y)==type(rayon)==float

    :Example:
    >>> get_y((230,220,10))
    220
    
    """
    return cercle[1]

def get_rayon(cercle):
    """
    renvoie le rayon du cercle passe en parametre

    :param cercle: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle et le rayon
    :type cercle: tuple
    :return: le rayon du cercle
    :rtype: float
    :UC: type(x)==type(y)==type(rayon)==float

    :Example:
    >>> get_rayon((230,230,10))
    10
    
    """
    return cercle[2]


