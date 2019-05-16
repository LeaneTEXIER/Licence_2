'''
   Compute the entropy on files.

   @author FIL - IEEA - Univ. Lille 1 (oct 2010, août 2015)
'''

import sys
from math import *


def entropy(filename): 
    '''
    Computes the entropy of the file called `filename`.

    :param filename: Input file name.
    :type filename: str
    :return: A tuple whose first element is an integer: the number of bytes read\
    and the second element is a float: the entropy of the file's content
    :rtype: tuple
    '''
    counters = {}
    '''
    Dictionary that will store the number of occurrences of each byte.
    '''
    total_sum = 0
    nb_bytes = 0
    # Read the file to count occurrences of each byte
    infile = open(filename, 'rb')
    byte = infile.read(1)
    while len(byte)!=0:
        if byte not in counters:
            counters[byte]=1
        else:
            counters[byte]+=1
        byte = infile.read(1)
        nb_bytes+=1
    for i in counters:
        total_sum+=counters[i]*(log(counters[i],2))
    entropy=log(nb_bytes, 2)-(total_sum/nb_bytes)
    infile.close()
    #Gain en taille si on code les octets de ce fichier avec un codage optimal
    G=(1-(entropy/8))*100
    return (nb_bytes, entropy, G)
    

def usage():
    print ("Usage: %s <filename>" % sys.argv[0])
    print ("\t<filename>: filename for which we want to compute the entropy.\n")
    exit(1)

def main():
    if len(sys.argv) != 2:
        usage()
    (nb_bytes, entro, gain) = entropy(sys.argv[1])
    print ("%d bytes read." % nb_bytes)
    print ("Entropy = %f bits per byte." % entro)
    print ("An optimal coding would reduce this file size by %f" % gain, "%.")
    
    
if __name__ == '__main__':
    main()
