'''
   Compute the entropy on files.

   @author FIL - IEEA - Univ. Lille 1 (oct 2010, août 2015)
'''

import sys

# IMPORTS A COMPLETER


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
    # A COMPLETER

    # Calcul de l'entropie à partir des effectifs des octets.
    # A COMPLETER


def usage():
    print ("Usage: %s <filename>" % sys.argv[0])
    print ("\t<filename>: filename for which we want to compute the entropy.\n")
    exit(1)

def main():
    if len(sys.argv) != 2:
        usage()
    (nb_bytes, entro) = entropy(sys.argv[1])
    print ("%d bytes read." % nb_bytes)
    print ("Entropy = %f bits per byte." % entro)
    
if __name__ == '__main__':
    main()
