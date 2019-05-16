# -*- coding: utf-8 -*-

"""
:mod:`CompactTrie` module : 

:author: Léane TEXIER & Antonio Viana SIMONE JUNIOR

:date: 2016, april
"""

mot=11##Pour éviter les collisions avec l'ajout de mot
def new_trie ():
    """
    :return: an empty compact trie
    """
    return {mot: False}


     
def add (n,w):
    """
    Add the word w in the compact trie n.
    
    :param n: The compact trie
    :type n: dict
    :param w: The word to add
    :type w: str
    :return: Trie n with the word w added
    :rtype: dict
    """
    commun=''
    clef=''
    k=0
    for i in n.keys():
        if (type(i)==str) and (w[0]==i[0]):
            clef=i
    if clef=='':
        n[w]=new_trie()
        n[w][mot]=True
        return n
    else:
        if w==clef:
            n[clef][mot]=True
            return n
        while k<len(clef) and k<len(w):
            if w[k]==clef[k]:
                commun=commun+w[k]
            else:
                break
            k+=1
        if commun==clef:
            (u,manquant)=w.split(clef)
            if len(n[clef].keys())<2:
                n[clef][manquant]=new_trie()
                n[clef][manquant][mot]=True
                return n
            else:
                add(n[clef],manquant)
        elif w==commun:
            (same,manquant)=clef.split(w)
            n[w]=new_trie()
            n[w][mot]=True
            n[w][manquant]=new_trie()
            n[w][manquant][mot]=True
            n[w][manquant]=n[clef]
            del(n[clef])
            return n
        else:
            (same,manquant1)=clef.split(commun)
            (same,manquant2)=w.split(commun)
            n[commun]=new_trie()
            n[commun][manquant1]=new_trie()
            n[commun][manquant1][mot]=True
            n[commun][manquant2]=new_trie()
            n[commun][manquant2][mot]=True
            n[commun][manquant1]=n[clef]
            del(n[clef])
            return n
    return n



def contains (n,w):
    """
    Test if the compact trie n contains the word w
    
    :param n: The compact trie
    :type n: dict
    :param w: The word to test
    :type w: str
    :return: True if the compact trie n contains the word w, False otherwise
    :rtype: bool
    """
    commun=''
    clef=''
    k=0
    for i in n.keys():
        if (type(i)==str) and (w[0]==i[0]):
            clef=i
    if clef=='':
        return False
    else:
        if w==clef:
            return n[w][mot]
        while k<len(clef) and k<len(w):
            if w[k]==clef[k]:
                commun=commun+w[k]
            else:
                break
            k+=1
        if commun==clef:
            (u,manquant)=w.split(clef)
            if len(n[clef].keys())<2:
                try:
                    return n[clef][manquant][mot]
                except:
                    return False
            else:
                return contains(n[clef],manquant)
        else:
            return False
        


def print_trie_aux(n,deb=0,cmp=0):
    """
    Print the lines describing nodes and the lines describing arcs
    
    :param n: The trie
    :type n: dict
    :param deb: The first number to take
    :type deb: int
    :param cmp: A counter
    :type cmp: int
    :return: Lines describing nodes and lines describing arcs
    :rtype: NoneType
    """
    if len(n.keys())>=2:
        t=0
        for c in n.keys():
            if c!=mot:
                if n[c][mot]==True:
                    print ('%d [style=filled,color=blue];' %(cmp+1))
                else:
                    print ('%d [style=filled,color=pink];' %(cmp+1))
                print('%d -> %d [label=" %s"];' % (deb,cmp+1,c))
                if t==1:
                    cmp = print_trie_aux(n[c],cmp+1,cmp+1)
                else:
                    cmp = print_trie_aux(n[c],deb+1,cmp+1)
                t=1
    if deb != 0:
        return cmp


    
def print_trie (n):
    """
    Print the lines describing nodes and the lines describing arcs with the begging and the end of the text to make a picture thanks to these lines
    
    :param n: The compact trie
    :type n: dict
    :return: Lines describing nodes and lines describing arcs and the begging and the end of the text
    :rtype: NoneType
    """
    print ('digraph G {')
    print_trie_aux(n)
    print ('}')
