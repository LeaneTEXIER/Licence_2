##TEXIER Léane
##Groupe 1

from coding import *

#Question 1 à 5: Cf tp4.txt


source_alphabet = \
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',\
     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

code1 = \
[ "00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111",
  "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111",
  "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111",
  "11000", "11001", "11111" ]

code2 = \
[".-/", "-.../", "-.-./", "-../", "./", "..-./", "--./", "..../", "../",
 ".---/", "-.-/", ".-../", "--/", "-./", "---/", ".--./", "--.-/", ".-./",
 ".../", "-/", "..-/", "...-/", ".--/", "-..-/", "-.--/", "--../", "---./"]

code3 = \
["1010", "0010011", "01001", "01110", "110", "0111100", "0111110",
 "0010010", "1000", "011111110", "011111111001", "0001", "00101",
 "1001", "0000", "01000", "0111101", "0101", "1011", "0110", "0011",
 "001000", "011111111000", "01111110", "0111111111", "01111111101",
 "111"]

#Question 6:
coding1=create(source_alphabet,code1)
coding2=create(source_alphabet,code2)
coding3=create(source_alphabet,code3)

#Question 7:
print('Question 7: Tests de codages et décodages')
print(coding1.code('L'))
print(coding1.decode('00100'))
print(coding2.code('A'))
print(coding2.decode('-./'))
print(coding3.code('E'))
print(coding3.decode('0111100'))
print('')

#Question 8:
def code_word(word, my_coding):
    """
    Code a word with the provided coding
    
    :param word: The word to be coded
    :type word: str
    :param my_coding: The coding to use for coding the word
    :type my_coding: Coding
    :return: Word coded with my_coding
    :rtype: str
    :CU: Symbols in the word are in the source alphabet of the coding	

    :Examples:
    >>> code_word('ABCD', coding1)
    '00000000010001000011'
    >>> code_word('', coding1)
    ''
    >>> code_word(' ZA', coding1)
    '111111100100000'
    """
    wc=''
    for i in word:
        wc=wc+my_coding.code(i)
    return wc

#Question 9:
print('Question 9: Codage du mot "CODAGE" suivant les trois codages (coding1, coding2, coding3)')
print(code_word('CODAGE', coding1))
print(code_word('CODAGE', coding2))
print(code_word('CODAGE', coding3))
print('')

#Question 10:
#len(my_coding_long_fixe.code(Coding.alphabet(my_coding_long_fixe)[0]))
#Coding.alphabet(my_coding_long_fixe)[0] permet de récuperer un symbole présent dans my_coding_long_fixe

#Question 11:
def decode_fixed_length_word(codeword, my_coding):
    """
    Decode a word using a fixed-length coding
    
    :param codeword: The codeword to be decoded
    :type codeword: str 
    :param my_coding: The coding to use for decoding the codeword
    :type my_coding: Coding
    :return: The result of decoding codeword with my_coding
    :rtype: str
    :CU: The codeword was obtained from the coding my_coding

    :Examples:
    >>> decode_fixed_length_word(code_word(''.join(source_alphabet), coding1), coding1)
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    >>> decode_fixed_length_word('111111100100000', coding1)
    ' ZA'
    >>> decode_fixed_length_word('', coding1)
    ''
    >>> decode_fixed_length_word('11111110010000', coding1)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_fixed_length_word: undecodable word
    """
    try:
        l=len(my_coding.code(Coding.alphabet(my_coding)[0]))
        wd=''
        for i in range(0,len(codeword),l):
            wd=wd+my_coding.decode(codeword[i:i+l])
        return wd
    except:
        raise Undecodable_word('decode_fixed_length_word: undecodable word')
    
#Question 12:
print('Question 12: Test de la fonction "decode_fixed_length_word"')
print(decode_fixed_length_word(code_word('CODAGE', coding1),coding1))
print('')

#Question 13:
print('Question 13: Décodage d une phrase avec la fonction "decode_fixed_length_word"')
print(decode_fixed_length_word('01011000001111101111001110100001\
01100000011011001100111100010111\
00111101000001001111100011001001\
11110101111111011101010010101100\
01010000010010001111110001000111\
00000100010111100100011011001101\
0000010010001',coding1))
print('')

#Question 14:
#Quelques tests
#>>>s='leane./'
#>>> s.find('ne')
#3
#>>> s.find('/')
#6
#>>> s.find('/.')
#-1

#Question 15:
def decode_comma_word(word, comma, my_coding):
    """
    Decode a word with the provided comma coding
    
    :param word: The word to be decoded
    :type word: str
    :param comma: The symbol used as a separator
    :type comma: str
    :param my_coding: The coding to use for coding the word
    :type my_coding: Coding
    :return: Word decoded with my_coding
    :rtype: str
    :CU: len(comma) == 1 and Symbols in the word are in the source alphabet of the coding

    :Examples:
    >>> decode_comma_word('-.-./---/-../.-/--././', '/', coding2)
    'CODAGE'
    >>> decode_comma_word(code_word(''.join(source_alphabet), coding2), '/', coding2)
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    >>> decode_comma_word('', '/', coding2)
    ''
    >>> decode_comma_word('-.../-.-', '/', coding2)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_comma_word: comma not found, cannot decode the word
    """
    assert len(comma)==1, 'The lengh of the comma is not 1'
    wd=''
    n=word.find(comma)
    while n!=-1:
        wd=wd+my_coding.decode(word[:n+1])
        word=word[n+1:]
        n=word.find(comma)
    if word!='':
        raise Undecodable_word('decode_comma_word: comma not found, cannot decode the word')
    return wd

#Question 16:
print('Question 16: Décodage d une phrase avec la fonction "decode_comma_word"')
print(decode_comma_word('.--./---/..-/.-./---./.-../.-/--\
-./..-./.-./.-/-./-.-././---./-.\
./---././-./---./-.../.-/.../---\
./-.././.../---./-./---/..-/../.\
-../.-.././.../---././-./-.-./--\
-/.-././', '/', coding2))
print('')


def decode_prefix_letter(word, my_coding):
    '''
    Decodes the first letter of the word, assuming a prefix coding was used.

    :param word: A word that was coded using `coding`
    :type word: str
    :param my_coding: The coding used for (de)coding
    :type my_coding: coding.Coding
    :return: a tuple whose elements are: 1) the symbol associated with the\
    first decodable prefix 2) the length of the first decodable prefix
    :rtype: tuple
    :CU: `word` was coded using `my_coding`
    :Examples:

    >>> decode_prefix_letter("0010010", coding3)
    ('H', 7)
    >>> decode_prefix_letter("00100101000", coding3)
    ('H', 7)
    >>> decode_prefix_letter("00", coding3)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_prefix_letter: no decodable prefix
    '''
    word_length = len(word)
    for i in range(1,word_length+1):
        try:
            prefix = my_coding.decode(word[:i])
            return (prefix, i)
        except:
            pass
    raise Undecodable_word

#Question 17:
print('Question 17: Décodage d une phrase avec la fonction "decode_prefix_letter"')
W='.--./---/..-/.-./---./.-../.-/--\
-./..-./.-./.-/-./-.-././---./-.\
./---././-./---./-.../.-/.../---\
./-.././.../---./-./---/..-/../.\
-../.-.././.../---././-./-.-./--\
-/.-././'
WD=''
while W!='':
    t=decode_prefix_letter(W,coding2)
    WD=WD+t[0]
    W=W[t[1]:]
print (WD)
print('')

#Question 18:
def decode_prefix_word(word, my_coding):
    """
    Decode a word with a prefix coding

    :param word: The word to be decoded
    :type word: str
    :param my_coding: the prefix coding that was used for coding the word
    :type my_coding: Coding
    :return: Word decoded with my_coding
    :rtype: str
    :CU: The word was coded using the coding my_coding

    :Examples:
    >>> decode_prefix_word("0010010", coding3)
    'H'
    >>> decode_prefix_word("00100101000", coding3)
    'HI'
    >>> decode_prefix_word(code_word(''.join(source_alphabet), coding3), coding3)
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    >>> decode_prefix_word("00", coding3)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word
    """
    wd=''
    while word!='':
        t=decode_prefix_letter(word,my_coding)
        wd=wd+t[0]
        word=word[t[1]:]
    return wd

#Question 19:
print('Question 19: Décodage d une phrase avec la fonction "decode_prefix_word"')
print(decode_prefix_word('01100010010101000011101011111110\
10110110111011000000011011111110\
00000011010110111111010111011110\
0101010000101110',coding3))
print('')


from tp2 import *
#Question 20:
def write_bits(stream, bits):
    """
    Write bits (a number multiple of 8) in a writable stream.

    :param steam: A steam opened in write and binary modes
    :param bits: A string made of binary characters
    :type bits: str
    :Action: Writes all the possible bits to the stream. We recall that bits can only be written byte per byte (8 bits per 8 bits).
    :return: The bits that have not been written yet to the stream.

    :Examples:
    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> write_bits(r, '11011111')
    ''
    >>> write_bits(r, '110')
    '110'
    >>> write_bits(r, '11011111000000010110')
    '0110'
    >>> r.seek(0) 
    0
    >>> list(r.read()) 
    [223, 223, 1]
    >>> write_bits(tempfile.NamedTemporaryFile(mode='w'), '11011111000000010110')
    Traceback (most recent call last):
    ...
    AssertionError: The stream must be opened in write and binary modes ('wb')
    """
    assert(stream.mode=='wb' or stream.mode=='rb+'),"The stream must be opened in write and binary modes ('wb')"
    for i in range (len(bits)//8):
        stream.write(bytes(binary_to_bytes(bits[:8])))
        bits=bits[8:]
    return (bits)

#Question 21:
def complete_byte(bits):
    """
    Completes a byte.

    :param bits: A binary string
    :type bits: str
    :return: A binary string of 8 bits which completes the string bits. The completion adds a 1 followed by as many zeroes as necessary to reach 8 bits.
    :rtype: str
    :CU: len(bits) < 8

    :Examples:
    >>> complete_byte('01')
    '01100000'
    >>> complete_byte('')
    '10000000'
    >>> complete_byte('0100001')
    '01000011'
    >>> complete_byte('00000001')
    Traceback (most recent call last):
    ...
    AssertionError: I cannot complete a completed byte!
    """
    assert (len(bits)<8), "I cannot complete a completed byte!"
    bits=bits+'1'
    while len(bits)!=8:
        bits=bits+'0'
    return bits

#Question 22:
def read_bits(stream):
    """
    Get the first 8 bits from the input stream.

    :param stream: The input stream which was opened in read and binary modes.
    :return: A binary string made of 8 bits (or an empty string)
    :rtype: str
    :CU: The stream was opened in read and binary modes.

    :Examples:
    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> write_bits(r, '1101111100000001')
    ''
    >>> r.seek(0)
    0
    >>> read_bits(r)
    '11011111'
    >>> read_bits(r)
    '00000001'
    >>> read_bits(r)
    ''
    """
    assert('rb' in stream.mode),"The stream must be opened in read and binary modes ('rb')"
    try:
        return (byte_to_binary(stream.read(1)[0]))
    except:
        return ('')

#Question 23:
def uncomplete_byte(bits):
    """
    The reverse function of complete_byte.

    :param bits: A string of 8 bits
    :type bits: str
    :return: A binary string of length < 8 for which the completion was removed (from the last 1-bit to the end).
    :rtype: str
    :CU: len(bits) == 8

    :Examples:
    >>> uncomplete_byte('01100000')
    '01'
    >>> uncomplete_byte('10000000')
    ''
    >>> uncomplete_byte('01000011')
    '0100001'
    >>> uncomplete_byte('0000000')
    Traceback (most recent call last):
    ...
    AssertionError: I can only uncomplete a byte
    """
    assert (len(bits)==8), "I can only uncomplete a byte"
    return (bits[:bits.rfind('1')])

#Question 24:
def remove_completion(bits):
    """
    Remove the completion bits from the end of a binary string.

    :param bits: A binary string of length >= 8 (which was already completed)
    :type bits: str
    :return: Return the binary string where the completion has been removed at the end (please note that the completion is done only on the last byte).
    :rtype: str
    :CU: len(bits) >= 8

    :Examples:
    >>> remove_completion('1010101010000000')
    '10101010'
    >>> remove_completion('1010101001100000')
    '1010101001'
    """
    assert (len(bits)>=8), "The lenght of the boits must be superior or equal to 8"
    b=''
    while len(bits)>8:
        b=b+bits[:8]
        bits=bits[8:]
    b=b+uncomplete_byte(bits)
    return (b)



def flush_binary_string(binary, stream):
    '''
    Flush a binary string by writing as many bytes as possible in the output
    stream.

    :param binary: A binary string
    :type binary: str
    :param stream: An output stream
    :return: the bits that could not be written in the output stream (the\
    length of the returned string is necessarily < 8).
    :Examples:

    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> flush_binary_string('01000001', r)
    ''
    >>> r.seek(0);
    0
    >>> r.read().decode()
    'A'
    '''
    while len(binary) >= 8:
        binary = write_bits(stream, binary)
    return binary

def write_binary_string_in_file(binary, file):
    '''
    Write the binary string in the file (the string is written 8 bits per 8
    bits in the file).
    As the binary string can have any length, the last byte will be completed
    so that all the content could be written to the file.

    :param binary: a binary string
    :type binary: str
    :param file: The filename of the file where the binary string will be\
    written
    :type file: str
    :Examples:

    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> write_binary_string_in_file('01000001010', r.name)
    >>> r.seek(0);
    0
    >>> r.read().decode()
    'AP'
    '''
    out_file = open(file, 'wb')
    binary = flush_binary_string(binary, out_file)
    write_bits(out_file, complete_byte(binary))
    out_file.close()

def read_file(file):
    '''
    Read the data in the file and returns a binary string corresponding to
    that data.

    :param file: the filanem of the file to read.
    :type file: str
    :return: The binary string of the data that was stored in the file. The\
    completion will be removed from the binary string.
    :rtype: str
    :Examples:

    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> write_binary_string_in_file('01000001010', r.name)
    >>> r.seek(0);
    0
    >>> read_file(r.name)
    '01000001010'
    '''
    in_file = open(file, 'rb')
    bits = ''
    binaire = read_bits(in_file)
    while binaire != '':
        bits += binaire
        binaire = read_bits(in_file)
    in_file.close
    if len(bits) > 0:
        bits = remove_completion(bits)
    return bits

#Question 25:
write_binary_string_in_file('01100010010101000011101011111110\
10110110111011000000011011111110\
00000011010110111111010111011110\
0101010000101110','mot3.data')
#La taille du fichier 'mot3.data' est de 15 octets.
#La longueur de la chaine mot3 est de 112 caractères.
#La taille du fichier correspond à la taille de la chaine divisée par 8 (car octets) plus 1.
#Le plus 1 vient du fait qu'un octet est utilisé pour coder le dernier bit (vide).

#Question 26:
print('Question 26: Lecture du contenu du fichier "mot3.data"')
print(read_file('mot3.data'))
#La chaine obtenue est bien identique à mot3.
