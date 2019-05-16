# -*- coding: utf-8 -*-

""":mod:`test` module : Test module for bloomfilter analysis

:author: Léane TEXIER & Antonio Viana SIMONE JUNIOR & `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2016, january

"""
import random
import bloomfilter

nb_hash_functions = 8
random_tab = [ 0 for i in range(128 * nb_hash_functions)]

def init_random_tab ():
    """
    Creates the hash functions.
    """
    global random_tab
    for i in range(128):
        for j in range(nb_hash_functions):
            random_tab[j * 128 + i] = random.randint(1,32000)

def code_of_string (str,n):
    """
    For a given string, returns the hash code for the n-th hashing function.
    
    :param str: The string to be hashed.
    :type str: string
    :param n: The function number.
    :type n: int
    :return: A hash code
    :rtype: int

    .. note:: 
       1 <= n <= nb_hash_functions
    """
    assert (1 <= n <= nb_hash_functions), "The n-th hashing function doesn't exist"
    h = 0
    for j in str:
        h+=random_tab[ord(j)+((n-1)*128)]  
    return h

def random_word ():
    """
    Returns a word with random letters whose length is between 4 and 7.

    :rtype: string
    """
    letters = [ chr(i) for i in range(ord('a'),ord('z')+1) ] + [ chr(i) for i in range(ord('A'),ord('Z')+1) ]
    length = 4 + random.randint(0,4)
    str = ""
    for i in range(length):
        str = str + random.choice(letters)
    return str

if __name__ == "__main__":
    init_random_tab()
##    bf = bloomfilter.create(2,code_of_string,8)
##    w = random_word()
##    bloomfilter.add(bf,"timoleon")
##    if bloomfilter.contains(bf,"timoleon"):
##        print("%s est present" % ('timoleon'))
##    if bloomfilter.contains(bf,w):
##        print("%s est present" % (w))
    s=set()
    while len(s)!=(2**10):
        w=random_word()
        s.add(w)
    I=[]
    for w in s:
        I.append(w)
    for n in range(1,9):
        for t in range (10,21):
            cmp_wtest=0
            cmp_fpos=0
            bf=bloomfilter.create(t,code_of_string,n)
            for w in I:
                bloomfilter.add(bf,w)
            for k in range(1,2**14+1):
                U= random_word()
                if U not in I:
                    cmp_wtest+=1
                    if bloomfilter.contains(bf,U):
                        cmp_fpos+=1
            print(t,bf['nb_function'],cmp_wtest,cmp_fpos,cmp_fpos/cmp_wtest)
        print()
        print()
