# -*- coding: utf-8 -*-

""":mod:`test` module : 

:author: Léane TEXIER & Antonio Viana SIMONE JUNIOR 

:date: 2016, march

"""

from tree import *

# Manipulation d'arbres binaires 

def arbre1 ():
    """
    :return: The first tree
    :rtype: dict
    """
    return create(12,create(9,empty_tree(),empty_tree()),create(8,empty_tree(),empty_tree()))

def arbre2 ():
    """
    :return: The second tree
    :rtype: dict
    """
    return create(12,create(9,empty_tree(),create(5,create(7,empty_tree(),empty_tree()),empty_tree())),empty_tree())

def arbre3 ():
    """
    :return: The third tree
    :rtype: dict
    """
    return  create(12,create(9,create(1,empty_tree(),empty_tree()),create(5,empty_tree(),empty_tree())),create(8,empty_tree(),create(4,create(7,empty_tree(),empty_tree()),create(6,empty_tree(),empty_tree()))))
    
def imprimer (tree):
    """
    Print the value of a tree with the infix manner
    :param tree: The tree
    :type tree: dict or None
    :return: nothing
    :print: The tree
    """
    if is_a_leaf(tree):
        print(tree['value'])
    elif not is_empty(tree):
        if not is_empty(get_left_son (tree)):
            imprimer(get_left_son (tree))
        print(get_root_value (tree))
        if not is_empty(get_right_son (tree)):
            imprimer(get_right_son (tree))
    

def taille (tree):
    """
    Return the size of the tree (if the tree is empty its size is -1)
    :param tree: The tree
    :type tree: dict or None
    :return: size of the tree
    :rtype: int
    """ 
    size=0
    if is_empty(tree):
        return -1
    elif is_a_leaf(tree):
        return 0
    else:
        if not is_empty(get_left_son (tree)):
            size+=1+taille(get_left_son (tree))
        if not is_empty(get_right_son (tree)):
            size+=1+taille(get_right_son (tree)) 
    return (size)


def hauteur (tree):
    """
    Return the height of the tree (if the tree is empty its height is -1)
    :param tree: The tree
    :type tree: dict or None
    :return: height of the tree
    :rtype: int
    """
    height=0
    if is_a_leaf(tree):
        return 0
    elif not is_empty(get_left_son (tree)) and not is_empty(get_right_son (tree)):
        height1=0
        height2=0
        height1+=hauteur(get_left_son (tree))
        height2+=hauteur(get_right_son (tree))
        height+=1+max(height1,height2)
    elif not is_empty(get_left_son (tree)):
        height+=1+hauteur(get_left_son (tree))
    elif not is_empty(get_right_son (tree)):
        height+=1+hauteur(get_right_son (tree))
    else:
        return -1
    return height

def nbFeuilles (tree):
    """
    Return the number of tree leaves 
    :param tree: The tree
    :type tree: dict or None
    :return: number of tree leaves
    :rtype: int
    """ 
    cmp_leaf=0
    if is_a_leaf(tree):
        return 1
    elif not is_empty(tree):
        if not is_empty(get_left_son (tree)):
            cmp_leaf+=nbFeuilles(get_left_son (tree))
        if not is_empty(get_right_son (tree)):
            cmp_leaf+=nbFeuilles(get_right_son (tree)) 
    return cmp_leaf

# Comptage d'arbres

def nbArbres (n):
    """
    Return the number of different possible topologies (calculate with a recursive algorithm)
    :param n: size of the tree
    :type n: int
    :return: number of different possible topologies 
    :rtype: int
    """
    cmp_topo=0
    if n==0:
        return 1
    else:
        for k in range (0,n):
            cmp_topo+=nbArbres(k)*nbArbres(n-k-1)
    return cmp_topo


def nbArbresEfficace (n):
    """
    Return the number of different possible topologies (calculate with an iterative algorithm using a board)
    :param n: size of the tree
    :type n: int
    :return: number of different possible topologies 
    :rtype: int
    """
    l=[1]
    for k in range (n+1):
        val=0
        for i in range(k+1):
            val+=l[i]*l[k-i]
        l.append(val)
    return l[n]

        
    
# Manipulation d'arbres binaires deherche 

def abr1 ():
    """
    :return: The first binary search tree
    :rtype: dict
    """
    return  create(6,create(4,create(2,create(1,empty_tree(),empty_tree()),empty_tree()),create(5,empty_tree(),empty_tree())),create(7,empty_tree(),empty_tree()))


def ajouter (value,tree):
    """
    Add a value to a tree
    :param value: Value to add
    :type value: int
    :param tree: The tree
    :type tree: dict or None
    :return: The tree with the value insert
    :rtype: dict    
    """
    if is_empty(tree):
        return create(value,empty_tree(),empty_tree())  
    else:
        root=get_root_value(tree)
        if value <=root:
            if is_empty(get_left_son(tree)):
                change_left(tree,create(value,empty_tree(),empty_tree()))
            else:
                ajouter(value,get_left_son(tree))
        else:
            if is_empty(get_right_son(tree)):
                change_right(tree,create(value,empty_tree(),empty_tree()))
            else:
                ajouter(value,get_right_son(tree))
    return tree
    

def abr2 ():
    """
    :return: The second binary search tree (create thanks to the function ajouter)
    :rtype: dict
    """
    l=[5,4,2,7,6,1]
    tree=empty_tree()
    for value in l:
        tree=ajouter(value,tree)
    return tree


def abr3 ():
    """
    :return: The third binary search tree (create thanks to the function ajouter)
    :rtype: dict
    """
    l=[7,1,4,5,6,2]
    tree=empty_tree()
    for value in l:
        tree=ajouter(value,tree)
    return tree

cmppt=0 ##
def appartient (value,tree):
    """
    Test if the value belongs to the tree or not
    :param value: Value to test
    :type value: int
    :param tree: The tree
    :type tree: dict or None
    :return: True if the value belongs to the tree, False otherwise
    :rtype: boolean 
    """
    global cmppt ##
    if is_empty(tree):
        return False
    else:
        root=get_root_value(tree)
        cmppt+=1
        if value==root:
            return True
        elif value<root:
            cmppt+=1
            if not is_empty(get_left_son(tree)):
                return appartient(value,get_left_son(tree))
            else:
                return False
        else:
            cmppt+=1
            if not is_empty(get_right_son(tree)):
                return appartient(value,get_right_son(tree))
            else:
                return False


def mini(tree):
    """
    Return the minimum value of the tree
    :param tree: tree
    :type tree: dict or not
    :return: The minimum value of the tree if it exists
    :rtype: int 
    """
    assert (is_empty(tree)==False), "The tree is empty, so there isn't (minimum) value"
    if is_empty(get_left_son(tree)):
        return get_root_value(tree)
    else:
        return mini(get_left_son(tree))


def maxi(tree):
    """
    Return the maximum value of the tree if it exists
    :param tree: tree
    :type tree: dict or not
    :return: The maximum value of the tree if it exists
    :rtype: int (or nothing)
    """
    assert (is_empty(tree)==False), "The tree is empty, so there isn't (maximum) value"
    if is_empty(get_right_son(tree)):
        return get_root_value(tree)
    else:
        return maxi(get_right_son(tree))

    
# Entier mysteri0eux 

def construitArbreEntierMysterieux(i,j):
    """
    Return the binary search tree who contains the values between i+1 and j-1
    :param i: First value (+1)
    :type i: int
    :param j: Last value (-1)
    :type j: int
    :return: Binary search tree with the values between i+1 and j-1
    :rtype: dict
    """
    mil=(i+j)//2
    if i==mil:
        return empty_tree()
    else:
        tree=create(mil,empty_tree(),empty_tree())
        change_left(tree,construitArbreEntierMysterieux(i,mil))
        change_right(tree,construitArbreEntierMysterieux(mil,j))
    return tree


def jouer (n):
    pass

# Tests sur les arbres binaires 
def testArbreBinaire (tree):
    imprimer(tree)
    print("")
    print("Taille    : %d" % (taille (tree)))
    print("Hauteur   : %d" % (hauteur (tree)))
    print("nbFeuilles: %d" % (nbFeuilles (tree)))

# Tests sur les arbres binaires de recherche 
def testABR (tree):
    imprimer(tree)
    print("")
    print("Taille    : %d" % (taille (tree)))
    print("Hauteur   : %d" % (hauteur (tree)))
    print("nbFeuilles: %d" % (nbFeuilles (tree)))
    print("Valeurs présentes dans l'arbre : ")
    for i in range(1,10+1):
        if appartient(i,tree): 
            print("%d " % i)
    print("")

# Programme principal 
if __name__ == "__main__":

    testArbreBinaire(arbre1())
    testArbreBinaire(arbre2())
    testArbreBinaire(arbre3())
    
##    for i in range(0,19+1):
##        print("(Version Recursive): Le nombre d'arbres à %d noeuds est %d" % (i,nbArbres(i)))
##        print("(Version Iterative): Le nombre d'arbres à %d noeuds est %d" % (i,nbArbresEfficace(i)))
  
    testABR(abr1())
    testABR(abr2())
    testABR(abr3())

    print("Arbre mysterieux entre 12 et 24:");
    imprimer (construitArbreEntierMysterieux(12,24))
    print("")
##    jouer(100);
