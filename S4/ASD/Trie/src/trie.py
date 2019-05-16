# -*- coding: utf-8 -*-

"""
:mod:`Trie` module : 

:author: Léane TEXIER & Antonio Viana SIMONE JUNIOR

:date: 2016, april
"""

def new_trie ():
    """
    :return: an empty trie
    """
    return {'mot': False}



def add (n,w):
    """
    Add the word w in the trie n.
    
    :param n: The trie
    :type n: dict
    :param w: The word to add
    :type w: str
    :return: Trie n with the word w added
    :rtype: dict
    """
    if w=='':
        return n
    taille=len(w)
    if w[0] in n:
        if taille==1:
            n[w[0]]['mot']=True
        else:
            add(n[w[0]],w[1:])
    else:
        n[w[0]]=new_trie()
        if taille==1:
            n[w[0]]['mot']=True
        else:
            add(n[w[0]],w[1:])
    return n



def contains (n,w):
    """
    Test if the trie n contains the word w
    
    :param n: The trie
    :type n: dict
    :param w: The word to test
    :type w: str
    :return: True if the trie n contains the word w, False otherwise
    :rtype: bool
    """
    if w=='':
        if n['mot']:
            return True
        else:
            return False
    elif w[0] in n:
        return contains(n[w[0]],w[1:])
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
            if c!='mot':
                if n[c]['mot']==True:
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
    
    :param n: The trie
    :type n: dict
    :return: Lines describing nodes and lines describing arcs and the begging and the end of the text
    :rtype: NoneType
    """
    print ('digraph G {')
    print_trie_aux(n)
    print ('}')



def printer(n):
    v=n.pop('mot')
    for i in n:
        print(i)
        printer(n[i])
