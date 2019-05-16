from tkinter import *
# -*- coding: utf-8 -*-

"""
TP AP2 PROJET
Licence 2 de mathématiques
Univ. Lille 1

cercles2.py

Module de création des badernes d'Apollonius contenant les fonctions soddy, les badernes et les recettes

"""

__author__ = 'DEBRAY Julie, FONTAINE Mallaury, TEXIER Léane'
__date_creation__ = 'novembre 2015'

### Import des modules ###
import points
import sys
from math import *

### Création du canvas ###
fenetre = Tk()
t = input (" taille du côté de la fênetre ")
canvas= Canvas(fenetre, width= t, height=t, background="white")
canvas.pack()
t= int(t)

### Variables globales ###
global liste_cercles
global liste_cercles_a_tracer
liste_cercles=[] # Liste de tous les cercles ( tuples (x,y,r))

### Augmntation de la récursivité ###
sys.setrecursionlimit (100000)

### Création du cercle ###
def create_cercle(cercle):
    """
    renvoie un cercle dans le canvas.

    :param cercle: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle et le rayon
    :type cercle: tuple
    :return: le cercle trace
    :rtype: None
    :UC: type(x)==type(y)==type(rayon)==int

    :Example:
    >>> get_x((400,400,230)
    
    
    """
    x= points.get_x(cercle)
    y= points.get_y(cercle)
    rayon= points.get_rayon(cercle)
    cercle = canvas.create_oval(x-rayon ,y- rayon ,x + rayon ,y + rayon)

### Création des cercles tangents ###
def tangents(c,n):
    """
    renvoie n cercles tangents au cercle c dans le canvas.

    :param c: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c et son rayon
    :type c: tuple
    :param n: Entier qui correspond au nombre de cercles que l'on veut tangents a c
    :type n: int
    :return: n cercles tangents a c a l'interieur de c
    :rtype: None
    :UC: type(x)==type(y)==type(rayon)==int
         type(n)==int
         

    :Example:
    >>> tangents((400,400,230),3)
    
    """
    global liste_cercles
    global liste_cercles_a_tracer
    liste_cercles_a_tracer=[]
    liste_annex=[]
    r_principal=points.get_rayon(c)
    r_centre=r_principal*(1-sin(pi/n))/(1+sin(pi/n))
    r_milieu=r_principal*sin(pi/n)/(1+sin(pi/n))
    create_cercle(c)
    x=points.get_x(c)
    y=points.get_y(c)
    pivot=(x,y,r_centre)
    create_cercle(pivot)
    liste_cercles.append(pivot)
    for i in range (n):
        x_i=(r_centre+r_milieu)*cos(2*i*pi/n)
        y_i=(r_centre+r_milieu)*sin(2*i*pi/n)
        cercle_i=(x_i+x,y_i+y,r_milieu)
        create_cercle(cercle_i)
        liste_cercles.append(cercle_i)
        liste_annex.append(cercle_i)
    l=liste_couple(n)
    for j in l:
        liste_cercles_a_tracer.append((pivot,liste_annex[j[0]],liste_annex[j[1]]))
        liste_cercles_a_tracer.append((c,liste_annex[j[0]],liste_annex[j[1]]))
    


    

def liste_couple(n):
    """
    Renvoie la liste des couples de cercles, c'est a dire ceux tangents deux a deux
    """
    l=[]
    for i in range (n):
        l=l+[(i,i+1)]
    return l[:n-1]+[(n-1,0)]



### Soddy ###

import cmath
def soddy(c1,c2,c3,rayon_minim):
    """
    renvoie le cercle tangent aux trois cercles c1, c2 et c3 dans le canvas.

    :param c1: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c1 et son rayon
    :type c1: tuple
    :param c2: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c2 et son rayon
    :type c2: tuple
    :param c3: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c3 et son rayon
    :type c3: tuple
    :param rayon_minim: rayon minimal pour pouvoir tracer le cercle
    :type rayon_minim: int
    :return: le cercle tangent à ces trois cercles c1, c2, c3 en meme temps
    :rtype: None
    :UC: type(x)==type(y)==type(rayon)==int==type(rayon_minim)
    
    """
    global liste_cercles
    global liste_cercles_a_tracer
    r1 = points.get_rayon(c1)
    r2 = points.get_rayon(c2)
    r3 = points.get_rayon(c3)
    #Les courbures
    k1= 1/r1
    k2= 1/r2
    k3 =1/r3
    if (r3>=r1) and (r3>=r2):
        if cercles_dans_cercle(c1,c2,c3):
            k3=-k3
    elif (r2>=r1) and (r2>=r3):
        if cercles_dans_cercle(c1,c3,c2):
            k2=-k2
    else:
        if cercles_dans_cercle(c2,c3,c1):
            k1=-k1
    # La courbure du cercle à tracer
    k4= k1+ k2 + k3 + 2* sqrt(k1*k2 +k1*k3 + k2 *k3)
    # Les complexes
    x1 = points.get_x(c1)
    x1= x1.real
    y1 = points.get_y(c1)
    y1 = y1.real
    x2 = points.get_x(c2)
    x2=x2.real
    y2 = points.get_y(c2)
    y2=y2.real
    x3 = points.get_x(c3)
    x3=x3.real
    y3 = points.get_y(c3)
    y3=y3.real
    z1 = complex(x1,y1)
    z2 = complex(x2,y2)
    z3 = complex(x3,y3)
    # Centre du cercle à tracer
    z41= (z1*k1 + z2 * k2 + z3*k3 - 2 * cmath.sqrt(k1*k2*z1*z2 + k2*k3*z2*z3 + k1*k3*z1*z3))/k4
    z42= (z1*k1 + z2 * k2 + z3*k3 + 2 * cmath.sqrt(k1*k2*z1*z2 + k2*k3*z2*z3 + k1*k3*z1*z3))/k4
    # coordonnées du centre du cercle à tracer
    x41= z41.real
    y41= z41.imag
    x42= z42.real
    y42= z42.imag
    ## Construction du cercle et enregistrement du cercle dans la liste si le rayon est supérieur à 1
    if (x41+y41)>(x42+y42):
        x4=x41
        y4=y41
    else:
        x4=x42
        y4=y42
    r4=1/k4
    if r4.real>rayon_minim.real:
        c4=(x4.real,y4.real,r4.real)
        create_cercle(c4)
        liste_cercles.append(c4)
        liste_cercles_a_tracer.append((c1,c2,c4))
        liste_cercles_a_tracer.append((c1,c3,c4))
        liste_cercles_a_tracer.append((c2,c3,c4))



def cercles_dans_cercle(c1,c2,c3):
    """Renvoie True si les cercles c1 et c2 sont dans c3, False sinon.

    :param c1: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c1 et son rayon
    :type c1: tuple
    :param c2: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c2 et son rayon
    :type c2: tuple
    :param c3: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c3 et son rayon
    :type c3: tuple
    :return: True si les cercles c1 et c2 sont dans c3, False sinon
    :rtype: Boolean
    :UC: type(x)==type(y)==type(rayon)==int
    """
    r1 = points.get_rayon(c1)
    r2 = points.get_rayon(c2)
    r3 = points.get_rayon(c3)
    x1 = points.get_x(c1)
    x2 = points.get_x(c2)
    x3 = points.get_x(c3)
    y1 = points.get_y(c1)
    y2 = points.get_y(c2)
    y3 = points.get_y(c3)
    if round((x3+r3),10)>=round((x2-r2),10)>=round((x3-r3),10) and round((x3+r3),10)>=round((x2+r2),10)>=round((x3-r3),10) and round((x3+r3),10)>=round((x1-r1),10)>=round((x3-r3),10) and round((x3+r3),10)>=round((x1+r1),10)>=round((x3-r3),10) and  round((y3+r3),10)>=round((y2-r2),10)>=round((y3-r3),10) and round((y3+r3),10)>=round((y2+r2),10)>=round((y3-r3),10) and round((y3+r3),10)>=round((y1-r1),10)>=round((y3-r3),10) and round((y3+r3),10)>=round((y1+r1),10)>=round((y3-r3),10):
        return True
    else:
        return False

### Badernes ###
    
def baderne(c,rayon_minim):
    global liste_cercles
    global liste_cercles_a_tracer
    if liste_cercles_a_tracer!=[]:
        soddy(liste_cercles_a_tracer[0][0], liste_cercles_a_tracer[0][1], liste_cercles_a_tracer[0][2], rayon_minim)
        liste_cercles_a_tracer.remove((liste_cercles_a_tracer[0]))
        baderne(c,rayon_minim)

    

def baderne_aux(c,n,rayon_minim):
    global liste_cercles
    global liste_cercles_a_tracer
    tangents(c,n)
    baderne(c,rayon_minim)



def remplir_cercles_vide(n,rayon_minim,rayon_minim2,i=0):
    global liste_cercles
    k=len(liste_cercles)
    if i<k:
        for j in range (i,k):
            if points.get_rayon(liste_cercles[j])>rayon_minim2:
                baderne_aux(liste_cercles[j],n,rayon_minim2)
        i=k        
        remplir_cercles_vide(n,rayon_minim,rayon_minim2,i)


def remplir_cercles_vide2(l,n,rayon_minim,rayon_minim2):
    if l!=[]:
        if points.get_rayon(l[0])>rayon_minim2:
            baderne_aux(l[0],n,rayon_minim)
        remplir_cercles_vide2(l[1:],n,rayon_minim,rayon_minim2)



###Reproduction des figures
#Nombre de cercles dépend de la distance au centre
#############


#Nombre de cercles intérieurs aléatoire
from random import randint
def remplir_cercles_vide_alea(l,rayon_minim,rayon_minim2):
    if l!=[]:
        if points.get_rayon(l[0])>rayon_minim2:
            n=randint(3,10)
            baderne_aux(l[0],n,rayon_minim)
        remplir_cercles_vide_alea(l[1:],rayon_minim,rayon_minim2)

def nbr_cercles_alea():
    """ Supposons taille de la fenetre au moins égale à 650"""
    baderne_aux((325,325,300),4,2)
    i=0
    long=0
    for i in range(3):
        l=liste_cercles[long:]
        long+=len(l)
        remplir_cercles_vide_alea(l,2,4)
        i+=1
    

#Toujours 7+1 cercles tangents
def figure_7plus1Tangents():
    """ Supposons taille de la fenetre au moins égale à 650"""
    baderne_aux((325,325,300),7,2)
    i=0
    long=0
    l=list()
    for i in range(2):
        l=liste_cercles[long:]
        long+=len(l)
        remplir_cercles_vide2(l,7,2,4)
        i+=1


#Toujours 5+1 cercles tangents
def figure_5plus1Tangents():
    """ Supposons taille de la fenetre au moins égale à 650"""
    baderne_aux((325,325,300),5,2)
    i=0
    long=0
    for i in range(3):
        l=liste_cercles[long:]
        long+=len(l)
        remplir_cercles_vide2(l,5,2,4)
        i+=1


###Nos recettes
def recette1():
    assert (t>=20)
    baderne_aux((t/2,t/2,(t/2)-20),100,1)
    i=0
    long=0
    l=liste_cercles[long:]
    while points.get_rayon(l[0])>50:
        long+=len(l)
        baderne_aux(l[0],100,1)
        l=liste_cercles[long:]


def recette2():
    assert (t>=20)
    j=32
    ##randint
    baderne_aux((t/2,t/2,(t/2)-20),j,1)
    i=0
    long=0
    l=liste_cercles[long:]
    while points.get_rayon(l[0])>10:
        j-=1
        long+=len(l)
        baderne_aux(l[0],j,1)
        l=liste_cercles[long:]


def recette3():
    assert (t>=20)
    j=randint(10,50)
    baderne_aux((t/2,t/2,(t/2)-20),j,1)
    i=0
    long=0
    l=liste_cercles[long:]
    while points.get_rayon(l[0])>10:
        j=randint(10,50)
        long+=len(l)
        baderne_aux(l[0],j,1)
        l=liste_cercles[long:]
    
