##TEXIER Léane
##Groupe 1

import struct

#Question 5:
def integer_to_digit(n):
    """
    Retourne le chiffre hexadécimal correspondant à n sous forme de caractère

    :param n: Entier décimal
    :type n: int
    :return: Chiffre n en hexadécimal
    :rtype: str
    :CU: n est un entier compris entre 0 et 15 inclus

    :Exemple:
    >>> integer_to_digit(15)
    'F'
    >>> integer_to_digit(0)
    '0'
    """
    assert (type(n)==int), "Le paramètre entré n'est pas un entier"
    assert (0<=n<=15), "L'entier entré n'est pas compris entre 0 et 15"
    if n<=9:
        return str(n)
    else:
        return chr(ord('7')+n)

#Question 6:
def integer_to_string(n,b):
    """
    Retourne l'écriture de l'entier n en base b

    :param n: Entier à convertir
    :type n: int
    :param b: Base dans laquelle convertir l'entier n
    :type n: int
    :return: L'entier n en base b
    :rtype: str
    :CU: Les deux paramètres sont des entiers, b est compris entre 0 et 36 et n est positif ou nul

    :Exemple:
    >>> integer_to_string(2000,16)
    '7D0'
    >>> integer_to_string(15,21)
    'F'
    """
    assert (type(n)==int), "Le nombre à convertir n'est pas un entier"
    assert (type(b)==int), "La base entrée n'est pas un entier"
    assert (0<=n), "Le nombre à convertir n'est pas positif ou nul"
    assert (0<=b<=36), "La base entrée n'est pas compris entre 0 et 36"
    if b>=10:
        if n<=9:
            return str(n)
        elif n<b:
            return chr(ord('7')+n)
        else:
            return (integer_to_string(n//b,b)+integer_to_string(n%b,b))
    else:
        if n<b:
             return str(n)
        else:
            return (integer_to_string(n//b,b)+integer_to_string(n%b,b))

#Question 10:
def deux_puissances(n):
    """
    Retourne la valeur de 2**n (à l'aide d'un opérateur logique)

    :param n: Puissance
    :type n: int
    :return: 2**n
    :rtype: int
    :CU: n est un entier positif ou nul

    :Exemple:
    >>> deux_puissances(12)
    4096
    >>> deux_puissances(9)
    512
    """
    assert (type(n)==int), "Le paramètre entré n'est pas un entier"
    assert (n>=0), "L'entier entré n'est pas positif ou nul"
    return 1<<n
            
#Question 12:
def integer_to_binary_str(n):
    """
    Retourne l'écriture binaire de l'entier n sous forme de chaîne de caractères
    
    :param n: Entier à convertir
    :type n: int
    :return: L'entier n en binaire
    :rtype: str
    :CU: n est un entier positif ou nul

    :Exemple:
    >>>integer_to_binary_str(132)
    '10000100'
    >>> integer_to_binary_str(21)
    '10101'
    """
    assert (type(n)==int), "Le paramètre entré n'est pas un entier"
    assert (n>=0), "L'entier entré n'est pas positif ou nul"
    b=''
    if n==0:
        b='0'
    else:
        while n>=1:
            b=str(n&1)+b
            n=n>>1
    return b

#Question 13:
def binary_str_to_integer(b):
    """
    Retourne l'entier correpondant au nombre binaire b
    
    :param b: Nombre binaire à convertir
    :type b: str
    :return: L'entier b en décimal
    :rtype: int
    :CU: b doit etre un nombre binaire

    :Exemple:
    >>> binary_str_to_integer('110100')
    52
    >>> binary_str_to_integer('11010110101')
    1717
    """
    assert (type(b)==str), "Le paramètre entré n'est pas une chaîne de caractères"
    assert ((i=='0' or i=='1') for i in b), "Le nombre entré n'est pas un chiffre binaire"
    n=0
    for i in range(len(b)):
        if b[i]=='0':
            n=n<<1
        else:
            n=(n<<1) | 1
    return n

#Question 14:
def byte_to_binary(o):
    """
    Retourne la valeur binaire sur 8 bits de l'octet entré en paramètre

    :param o: Octet à convertir
    :type o: str
    :return: L'octet o en binaire
    :rtype: str
    :CU: o doit être un octet

    :Exemple:
    >>> byte_to_binary(10)
    '00001010'
    >>> byte_to_binary(126)
    '01111110'
    """
    assert (type(o)==int), "Le paramètre entré n'est pas un entier (octet)"
    assert (0<=o<256), "Le paramètre entré n'est pas un octet (valeur comprise entre 0 et 255 inclus)"
    b=integer_to_binary_str(o)
    while len(b)!=8:
        b='0'+b
    return b

#Question 15:
def float_to_bin (n):
    """
    Retourne la chaine binaire correspondant au réel n

    :param n: Réel 
    :type n: int or float
    :return: Chaine binaire du réel n
    :rtype: str
    :CU: n est un réel

    :Exemple:
    >>> float_to_bin(3.5)
    '01000000011000000000000000000000'
    >>> float_to_bin(1)
    '00111111100000000000000000000000'
    """
    assert (type(n)==float or type(n)==int), "Le paramètre entré n'est pas un réel"
    b=''
    bytes_stored = struct.pack('>f', n)
    for i in bytes_stored:
        b=b+byte_to_binary(i)
    return b

#Question 16:
def change_a_bit(b,p):
    """
    Retourne la chaine binaire b entré en remplacant le bit à la position p par son bit inverse

    :param b: Chaine binaire
    :type b: str
    :param p: Position du bit à inverser
    :type p: int
    :CU: b doit etre une chaine binaire et p un entier (compris entre 0 et len(b)-1)

    :Exemple:
    >>> change_a_bit('01011',2)
    '01111'
    >>> change_a_bit('010101011',1)
    '000101011'
    """
    assert (type(b)==str), "Le paramètre b entré n'est pas une chaîne de caractères"
    assert (type(p)==int), "Le paramètre p entré n'est pas un entier"
    assert (0<=p<len(b)), "Le paramètre p entré doit être compris entre 0 et la longueur de la chaine b-1"
    return b[:p]+str(int(b[p])^1)+b[p+1:]

#Question 17:
def binary_to_bytes(b):
    """
    Retourne la chaine binaire b en une liste d'entiers correspondants à chaque groupe de 8 bits contenus dans b

    :param b: Chaine binaire
    :type b: str
    :return: Liste d'entiers
    :rtype: list
    :CU: b est une chaine binaire ayant une taille d'un multiple de 8

    :Exemple:
    >>> binary_to_bytes('0101101001010010')
    [90, 82]
    >>> binary_to_bytes('110101101101011111011000')
    [214, 215, 216]
    """
    assert (type(b)==str), "Le paramètre b entré n'est pas une chaîne de caractères"
    assert (len(b)%8==0), "La longueur de la chaine b doit être un multiple de 8"
    l=[]
    while len(b)>0:
        bi=b[:8]
        l.append(binary_str_to_integer(bi))
        b=b[8:]
    return l
    
#Question 18:
def change_a_bit_in_float(n,p):
    """
    Retourne la valeur du réel modifié (=prend la représentation binaire de n et change son bit se trouvant à la position p)

    :param n: Réel à modifier
    :type n: int or float
    :param p: Position du bit à inverser
    :type p: int
    :return: Valeur du réel n modifié (inversion du bit à la position b dans la représentation binaire de n)
    :rtype: float
    :CU: n est un réel et p est un réel positif inférieur strictement à 32 (4 octets)

    :Exemple:
    >>> change_a_bit_in_float(3.5,10)
    3.0
    >>> change_a_bit_in_float(3.5,14)
    3.53125
    """
    assert (type(n)==float or type(n)==int), "Le paramètre entré n'est pas un réel"
    assert (type(p)==int), "Le paramètre p entré n'est pas un entier"
    assert (0<=p<32), "p doit être un réel positif inférieur strictement à 32"
    b=change_a_bit(float_to_bin(n),p)
    l=binary_to_bytes(b)
    return (struct.unpack('>f', bytes(l))[0])

#Question 29: 
def isolatin_to_utf8(stream):
    """
    Lit un caractère ISO-8859-1 du flux 'stream' et retourne un tuple d'un ou deux octet(s) correspondant(s) au caractère UTF-8.
    Si on est à la fin du fichier, retourne None

    :param stream: flux
    :return: Tuple d'un ou deux octet(s) correspondant(s) au caractère UTF-8 (ou None si fin du fichier)
    :rtype: tuple
    :CU: None
    """
    try:
        byte = stream.read(1)[0]
        if byte<160:
            return (byte,)
        else:
            return (((byte>>6)|192),((byte | 192) & 191))
    except IndexError:
        stream.close()
        return None

#Question 30:
def convert_file(source, dest, conversion):
    '''
    Convert `source` file using the `conversion` function and writes the
    output in the `dest` file.

    :param source: The name of the source file
    :type source: str
    :param dest: The name of the destination file
    :type dest: str
    :param conversion: A function which takes in parameter a stream (opened\
    in read and binary modes) and which returns a tuple of bytes.
    :type conversion: function
    '''
    entree = open(source, 'rb')
    sortie = open(dest, 'wb')
    octets_sortie = conversion(entree)
    while octets_sortie != None:
        sortie.write(bytes(octets_sortie))
        octets_sortie = conversion(entree)
    sortie.close()

def convert_file_isolatin_utf8(source, dest):
    '''
    Converts `source` file from ISO-8859-1 encoding to UTF-8.
    The output is written in the `dest` file.
    '''
    convert_file(source, dest, isolatin_to_utf8)

#convert_file_isolatin_utf8('cigale-ISO-8859-1.txt','cigale30-UTF-8.txt')

#Question 31:
def utf8_to_isolatin(stream):
    """
    Lit un caractère UTF-8 du flux 'stream' et retourne un tuple d'un octet correspondant au caractère ISO-8859-1
    Si on est à la fin du fichier, retourne None

    :param stream: flux
    :return: Tuple d'un octet correspondant au caractère ISO-8859-1 (ou None si fin du fichier)
    :rtype: tuple
    :CU: None
    """
    try:
        byte = stream.read(1)[0]
        if (byte==194):
            byte2=stream.read(1)[0]
            return (byte2,)
        elif (byte==195):
            byte2=stream.read(1)[0]
            return ((byte2+64),)
        else:
            return (byte,)
    except IndexError:
        stream.close()
        return None

#Question 32:
def conversion_file_utf8_isolatin(source, dest):
    '''
    Converts `source` file from UTF-8 encoding to ISO-8859-1.
    The output is written in the `dest` file.
    '''
    convert_file(source, dest, utf8_to_isolatin)

#conversion_file_utf8_isolatin('cigale-UTF-8.txt','cigale32-ISO-8859-1.txt')
