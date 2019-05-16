# -*- coding: utf-8 -*-

"""
TP AP2 PROJET
Licence 2 de mathématiques
Univ. Lille 1

cercles1.py

Module de création des badernes d'Apollonius contenant les fonctions soddy, les badernes et les recettes

"""

__author__ = 'DEBRAY Julie, FONTAINE Mallaury, TEXIER Léane'
__date_creation__ = 'novembre 2015'


### Import des modules ###
from tkinter import *
import points
from math import *
import sys

### Création du Canvas ###
fenetre = Tk()
t = input (" taille du côté de la fênetre ")
canvas= Canvas(fenetre, width= t, height=t)
canvas.pack()
t= int(t)


### Variables globales ###
global liste_cercles
global liste_triplets_petits
global liste_triplets_grands
liste_cercles=[] # Liste de tous les cercles ( tuples (x,y,r))
liste_triplets_petits=[] # Liste de triplets de cercles utilisant soddy
liste_triplets_grands=[] # Liste de tuples de cercles utlisant soddy_g

### Augmentation de la récursivité ###
sys.setrecursionlimit (100000)

###  Creation d'un cercle ###
def create_cercle(cercle):
    """
    renvoie un cercle dans le canvas.

    :param cercle: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle et le rayon
    :type cercle: tuple
    :return: le cercle trace
    :rtype: None
    :UC: type(x)==type(y)==type(rayon)==float

    :Example:
    >>> get_x((400,400,230))
    
    
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
    :UC: type(x)==type(y)==type(rayon)==float
         type(n)==int
         

    :Example:
    >>> tangents((400,400,230),3)
    
    """
    global liste_cercles
    global liste_triplets_petits
    global liste_triplets_grands
    r_principal=points.get_rayon(c)
    r_centre=r_principal*(1-sin(pi/n))/(1+sin(pi/n))
    r_milieu=r_principal*sin(pi/n)/(1+sin(pi/n))
    create_cercle(c)
    x=points.get_x(c)
    y=points.get_y(c)
    create_cercle((x,y,r_centre))
    liste_cercles.append((x,y,r_centre))
    for i in range (n):
        x_i=(r_centre+r_milieu)*cos(2*i*pi/n)
        y_i=(r_centre+r_milieu)*sin(2*i*pi/n)
        create_cercle((x_i+x,y_i+y,r_milieu))
        liste_cercles.append((x_i+x,y_i+y,r_milieu))
    l=liste_couple(n)
    for w in range (n):
        rayon1= points.get_rayon(liste_cercles[l[w][0]+1])
        rayon2= points.get_rayon(liste_cercles[l[w][1]+1])
        rayon3= points.get_rayon(liste_cercles[0])
        if rayon1>rayon2 and rayon1>rayon3:
            liste_triplets_petits.append((liste_cercles[l[w][1]+1],liste_cercles[0],liste_cercles[l[w][0]+1]))
        elif rayon2>rayon1 and rayon2>rayon3:
            liste_triplets_petits.append((liste_cercles[0],liste_cercles[l[w][0]+1],liste_cercles[l[w][1]+1]))
        else:
            liste_triplets_petits.append((liste_cercles[l[w][0]+1],liste_cercles[l[w][1]+1],liste_cercles[0]))
        liste_triplets_grands.append((liste_cercles[l[w][0]+1],liste_cercles[l[w][1]+1]))

### Les fonctions soddy ###
import cmath
def soddy(c1,c2,c3,rayon_minim):
    """
    renvoie le cercle tagent aux trois cercles c1, c2 et c3 dans le canvas.

    :param c1: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c1 et son rayon
    :type c1: tuple
    :param c2: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c2 et son rayon
    :type c2: tuple
    :param c3: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c3 et son rayon
    :type c3: tuple
    :param rayon_minim: taille minimum du rayon de chaque cercle (critere d'arret)
    :type rayon_minim: float   
    :return: le cercle tangent à ces trois cercles c1, c2, c3 en meme temps
    :rtype: None
    :UC: type(x)==type(y)==type(rayon)==float

    :Example:
    
    """
    global liste_cercles
    global liste_delete2
    global liste_new
    r1 = points.get_rayon(c1)
    r2 = points.get_rayon(c2)
    r3 = points.get_rayon(c3)
    #Les courbures
    k1= 1/r1
    k2= 1/r2
    k3 =1/r3
    # La courbure du cercle à tracer
    k4= k1+ k2 + k3 + 2* sqrt(k1*k2 +k1*k3 + k2 *k3)
    # Les complexes
    x1 = points.get_x(c1)
    y1 = points.get_y(c1)
    x2 = points.get_x(c2)
    y2 = points.get_y(c2)
    x3 = points.get_x(c3)
    y3 = points.get_y(c3)
    z1 = complex(x1,y1)
    z2 = complex(x2,y2)
    z3 = complex(x3,y3)
    # Centre du cercle à tracer
    z4= (z1*k1 + z2 * k2 + z3*k3 + 2 * cmath.sqrt(k1*k2*z1*z2 + k2*k3*z2*z3 + k1*k3*z1*z3))/k4
    ## coordonnées du centre du cercle à tracer
    x4= z4.real
    y4= z4.imag
    ## Construction du cercle et enregistrement du cercle dans la liste si le rayon est supérieur à 1
    r4=1/k4
    if r4>rayon_minim:
        create_cercle((x4,y4,r4))
        liste_cercles.append((x4,y4,r4))
        liste_new.append((x4,y4,r4))
    else:
        liste_delete2.append((c1,c2,c3))

                  
    

        
import cmath
def soddy_g(c1,c2,c3,rayon_minim):
    """
    renvoie le cercle tangent aux trois cercles c1, c2 et c3 dans le canvas. 

    :param c1: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c1 et son rayon
    :type c1: tuple
    :param c2: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c2 et son rayon
    :type c2: tuple
    :param c3: represente TOUJOURS le grand cercle, c'est un tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c3 et son rayon
    :type c3: tuple
    :param rayon_minim: taille minimum du rayon de chaque cercle (critere d'arret)
    :type rayon_minim: float  
    :return: le cercle tangent à ces trois cercles c1, c2, c3 en meme temps
    :rtype: None
    :UC: type(x)==type(y)==type(rayon)==float

    :Example:
      
    """
    global liste_cercles
    global liste_triplets_grands
    global liste_new2
    r1 = points.get_rayon(c1)
    r2 = points.get_rayon(c2)
    r3 = points.get_rayon(c3)
    assert r3>=r1 and r3>=r2
    # Les courbures
    k1= 1/r1
    k2= 1/r2
    k3 =-(1/r3)
    # La courbure du cercle à tracer
    k4= k1+ k2 + k3 + 2*cmath.sqrt(k1*k2 +k1*k3 + k2 *k3)
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
        create_cercle((x4.real,y4.real,r4.real))
        liste_cercles.append((x4.real,y4.real,r4.real))
        liste_new2.append((x4.real,y4.real,r4.real))
    else:
        liste_delete.append((c1,c2))

    
        

def liste_couple(n):
    """
    Renvoie la liste des couples de cercles, c'est a dire ceux tangents deux a deux
    :param n: Nombre de cercles tangents
    :type n: int
    :return: La liste de tous les cercles tangents deux a deux
    :rtype: list
    """
    l=[]
    for i in range (n):
        l=l+[(i,i+1)]
    return l[:n-1]+[(n-1,0)]

### Création de la première baderne ###

def create_liste_tpetits():
    """
    Cree une liste des petits cercles
    
    :return: une liste composee de triplets. ces triplets representent les petits cercles deja construits, c'est a dire, leurs coordonnees x et y et leur rayon
    :rtype: list

    :Example:
    >>> create_liste_tpetits()
    [(230,230,10),(110,110,15)...]
    """
    global liste_triplets_petits
    global liste_new
    global liste_triplets_grands
    global liste_new2
    liste_tpetits=[]
    for i in range (len(liste_new)):
        liste_tpetits.append((liste_triplets_petits[i][0],liste_triplets_petits[i][1],liste_new[i]))
        liste_tpetits.append((liste_triplets_petits[i][1],liste_triplets_petits[i][2],liste_new[i]))
        liste_tpetits.append((liste_triplets_petits[i][2],liste_triplets_petits[i][0],liste_new[i]))
    for j in range (len(liste_new2)):
        liste_tpetits.append((liste_triplets_grands[j][0],liste_triplets_grands[j][1],liste_new2[j]))
    liste_triplets_petits = liste_tpetits


def create_liste_tgrands():
    """
    Cree une liste des grands cercles
    
    :return: une liste composee de triplets. ces triplets representent les grands cercles deja contruits, c'est a dire, leurs coordonnees x et y et leur rayon
    :rtype: list

    :Example:
    >>> create_liste_tgrands()
    [(230,230,10),(110,110,15)...]
    """
    global liste_triplets_grands
    global liste_new2
    liste_tgrands=[]
    for j in range (len(liste_new2)):
        liste_tgrands.append((liste_triplets_grands[j][0],liste_new2[j]))
        liste_tgrands.append((liste_triplets_grands[j][1],liste_new2[j]))
    liste_triplets_grands = liste_tgrands


def baderne(c,rayon_minim):
    """
    Fonction recursive qui cree les cercles tangents les uns aux autres, cette fonction sert pour baderne_aux 

    :param c: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c et son rayon
    :type c: tuple
    :param rayon_minim: taille minimum du rayon de chaque cercle (critere d'arret)
    :type rayon_minim: float  
    :return: None (enregistre les cercles pour tracer avec baderne_aux)
    :rtype: None
    :UC: type(x)==type(y)==type(rayon)==float

    :Example:
      
    """    
    global liste_cercles
    global liste_triplets_petits
    global liste_triplets_grands
    global liste_new
    global liste_new2
    global liste_delete
    global liste_delete2
    liste_new=[]
    liste_new2=[]
    liste_delete=[]
    liste_delete2=[]
    if (liste_triplets_petits!=[]) or (liste_triplets_grands!=[]):
        for i in range (len(liste_triplets_petits)):
            soddy(liste_triplets_petits[i][0],liste_triplets_petits[i][1],liste_triplets_petits[i][2],rayon_minim)
        for j in range (len(liste_triplets_grands)):
            rayon1 = points.get_rayon(liste_triplets_grands[j][0])
            rayon2 = points.get_rayon(liste_triplets_grands[j][1])
            rayon3 = points.get_rayon(c)
            if rayon1>=rayon2 and rayon1>=rayon3:
                soddy_g(c,liste_triplets_grands[j][1],liste_triplets_grands[j][0],rayon_minim)
            elif rayon2>rayon1 and rayon2>=rayon3:
                soddy_g(c,liste_triplets_grands[j][0],liste_triplets_grands[j][1],rayon_minim)
            else:
                soddy_g(liste_triplets_grands[j][0],liste_triplets_grands[j][1],c,rayon_minim)
        for k in range (len(liste_delete)):
            if liste_delete[k] in liste_triplets_grands:
                liste_triplets_grands.remove(liste_delete[k])
        for m in range (len(liste_delete2)):
            liste_triplets_petits.remove(liste_delete2[m])
        create_liste_tpetits()
        create_liste_tgrands()
        baderne(c,rayon_minim)

    

def baderne_aux(c,n,rayon_minim):
    """
    Renvoie l'ensemble des n cercles tangents a c dans le canvas. C'est une recursivite qui dessine des cercles tangents dans des cercles tangents 

    :param c: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c et son rayon
    :type c: tuple
    :param rayon_minim: taille minimum du rayon de chaque cercle (critere d'arret)
    :type rayon_minim: float  
    :return: l'ensemble des cercles dans le canvas
    :rtype: None
    :UC: type(x)==type(y)==type(rayon)==float

    :Example:
      
    """
    global liste_cercles
    global liste_triplets_petits
    global liste_triplets_grands
    tangents(c,n)
    baderne(c,rayon_minim)


### Les recettes ###
def recette1(c,n,n2,rayon_minim1, rayon_minim2):
    """
    renvoie l'une des recettes dans le canvas. 

    :param c: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c et son rayon
    :type c: tuple
    :param n: Nombre de cercles tangents qu'on veut
    :type n: int
    :param n2: Nombre de cercles tangents qu'on veut pour la recursivite interieure (les badernes interieures)
    :type n2: int
    :param rayon_minim1: taille minimum du rayon de chaque cercle (critere d'arret)
    :type rayon_minim1: float
    :param rayon_minim2: taille minimum du rayon de chaque cercle (critere d'arret de la deuxieme recursivite, celle des badernes interieures)
    :type rayon_minim2: float  
    :return: l'ensemble des cercles tangents dans le canvas selon nos gouts
    :rtype: None
    :UC: type(x)==type(y)==type(rayon)==float

    :Example:
      
    """
    global liste_cercles
    global liste_cercles_aux
    baderne_aux(c,n,rayon_minim1)
    liste_cercles_aux=liste_cercles
    liste_cercles=liste_cercles[len(liste_cercles):]
    for i in range (len(liste_cercles_aux)):
        baderne_aux(liste_cercles_aux[i],n2,rayon_minim2)
        liste_cercles_aux = liste_cercles_aux + liste_cercles
        liste_cercles=liste_cercles[len(liste_cercles):]
        n+=1
        
    

import random 
def recette2(c,n,rayon_minim1, rayon_minim2):
    """
    renvoie l'une des recettes dans le canvas. 

    :param c: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c et son rayon
    :type c: tuple
    :param n: Nombre de cercles tangents qu'on veut
    :type n: int
    :param rayon_minim1: taille minimum du rayon de chaque cercle (critere d'arret)
    :type rayon_minim1: float
    :param rayon_minim2: taille minimum du rayon de chaque cercle des badernes interieures(critere d'arret de la deuxieme recursivite)
    :type rayon_minim2: float  
    :return: l'ensemble des cercles tangents dans le canvas selon nos gouts
    :rtype: None
    :UC: type(x)==type(y)==type(rayon)==float

    :Example:
      
    """
    global liste_cercles
    global liste_cercles_aux
    baderne_aux(c,n,rayon_minim1)
    liste_cercles_aux=liste_cercles
    liste_cercles=liste_cercles[len(liste_cercles):]
    for i in range (len(liste_cercles_aux)):
        n2= random.randint(3,20)
        baderne_aux(liste_cercles_aux[i],n2,rayon_minim2)
        liste_cercles_aux = liste_cercles_aux + liste_cercles
        liste_cercles =liste_cercles[len(liste_cercles):]
        i+=1



def recette3(c,rayon_min):
    """
    renvoie l'une des recettes dans le canvas. 

    :param c: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c et son rayon
    :type c: tuple
    :param rayon_min: taille minimum du rayon de chaque cercle (critere d'arret)
    :type rayon_min: float
    :return: l'ensemble des cercles tangents dans le canvas selon nos gouts
    :rtype: None
    :UC: type(x)==type(y)==type(rayon)==float

    :Example:
      
    """
    global liste_cercles
    global liste_cercles_aux
    baderne_aux(c,50,rayon_min)
    liste_cercles_aux=liste_cercles
    liste_cercles=liste_cercles[len(liste_cercles):]
    i=2
    while points.get_rayon(liste_cercles_aux[0]) > rayon_min:
        baderne_aux(liste_cercles_aux[0],int(5*i),rayon_min)
        liste_cercles_aux=liste_cercles
        liste_cercles=liste_cercles[len(liste_cercles):]
        i+=0.5

def recette4(c,n,rayon_min):
    """
    renvoie l'une des recettes dans le canvas. 

    :param c: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c et son rayon
    :type c: tuple
    :param n: nombre de cercles tangents au cercle c
    :type n: int
    :param rayon_min: taille minimum du rayon de chaque cercle (critere d'arret)
    :type rayon_min: float
    :return: l'ensemble des cercles tangents dans le canvas selon nos gouts
    :rtype: None
    :UC: type(x)==type(y)==type(rayon)==float

    :Example:
      
    """
    global liste_cercles
    global liste_cercles_aux
    baderne_aux(c,n,rayon_min)
    liste_cercles_aux=liste_cercles
    liste_cercles=liste_cercles[len(liste_cercles):]
    i=1
    while points.get_rayon(liste_cercles_aux[0]) > rayon_min:
        baderne_aux(liste_cercles_aux[0],int(n),rayon_min)
        liste_cercles_aux=liste_cercles
        liste_cercles=liste_cercles[len(liste_cercles):]
        i+=1

       
def recette5(c,n,rayon_min):
    """
    renvoie l'une des recettes dans le canvas. 

    :param c: tuple de 3 chiffres, coordonnee x, coordonnee y du centre du cercle c et son rayon
    :type c: tuple
    :param n: nombre de cercles tangents au cercle c
    :type n: int
    :param rayon_min: taille minimum du rayon de chaque cercle (critere d'arret)
    :type rayon_min: float
    :return: l'ensemble des cercles tangents dans le canvas selon nos gouts
    :rtype: None
    :UC: type(x)==type(y)==type(rayon)==float

    :Example:
      
    """
    global liste_cercles
    global liste_cercles_aux
    baderne_aux(c,n,rayon_min)
    liste_cercles_aux=liste_cercles
    liste_cercles=liste_cercles[len(liste_cercles):]
    while points.get_rayon(liste_cercles_aux[0]) > rayon_min:
        n2=random.randint(5,50)
        baderne_aux(liste_cercles_aux[0],n2,rayon_min)
        liste_cercles_aux=liste_cercles
        liste_cercles=liste_cercles[len(liste_cercles):]
