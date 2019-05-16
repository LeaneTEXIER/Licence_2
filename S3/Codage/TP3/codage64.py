##TEXIER Léane
##Groupe 1

#Question 2:
#Supposons q la taille du fichier en octets.
#Pour que le fichier ne possède aucun symbole '=': il faut que q%3==0
#Pour que le fichier possède un symbole '=': il faut que q%3==2
#Pour que le fichier possède deux symboles '=': il faut que q%3==1


BASE64_SYMBOLS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                  'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                  'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                  'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                  'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                  'w', 'x', 'y', 'z', '0', '1', '2', '3',
                  '4', '5', '6', '7', '8', '9', '+', '/']

#Question 3 :
#BASE64_SYMBOLS[1]
#BASE64_SYMBOLS[61]


#Question 4:
def bytes_to_symbols(data):
    """
    Takes (at most) three bytes of data in input and returns the corresponding bas64 symbols.
    
    :param data: A list of at most three bytes
    :type data: list
    :return: Four base64 symbols (or ‘=’) corresponding to the data given in input
    :rtype: str
    :CU: len(data) <= 3

    :Examples:
    >>> bytes_to_symbols([5])
    'BQ=='
    >>> bytes_to_symbols([4, 163])
    'BKM='
    >>> bytes_to_symbols([28, 89, 101])
    'HFll'
    >>> bytes_to_symbols([])
    ''
    """
    assert (len(data)<=3), "The lenght of the list is inferior or equal to 3"
    if len(data)==0:
        return ''
    else:
        b=''
        for octet in data:
            bi=bin(octet)[2:]
            while len(bi)<8:
                bi='0'+bi
            b+=bi
        if len(data)==1:
            return (BASE64_SYMBOLS[int(b[:6],2)]+BASE64_SYMBOLS[int((b[6:]+'0000'),2)]+'==')
        elif len(data)==2:
            return (BASE64_SYMBOLS[int(b[:6],2)]+BASE64_SYMBOLS[int(b[6:12],2)]+BASE64_SYMBOLS[int((b[12:]+'00'),2)]+'=')
        else:
            return (BASE64_SYMBOLS[int(b[:6],2)]+BASE64_SYMBOLS[int(b[6:12],2)]+BASE64_SYMBOLS[int(b[12:18],2)]+BASE64_SYMBOLS[int(b[18:],2)])

            
#Question 5 et 6:     
def  base64_encode(source):
    '''
    Encode a file in base64 and outputs the result on standard output.

    :param source: the source filename
    :type source: str
    '''
    input = open(source, 'rb')
    data = input.read(3)
    nb = 0
    while len(data) > 0:
        print (bytes_to_symbols(data), end='')
        nb+=1
        if nb==19: #76/4=19
            print('')
            nb=0
        data = input.read(3)
    print()
    input.close()


#Question 7:
def decode_base64_symbol(symbol):
    """
    Convert a base64 symbol in integer.
    
    :param symbol: The symbol to be converted
    :type symbol: str
    :return: The integer corresponding to the base64 symbol
    :rtype: int
    :CU: The symbol is part of the base64 symbols

    :Examples:
    >>> decode_base64_symbol('z')
    51
    >>> decode_base64_symbol('A')
    0
    >>> decode_base64_symbol('/')
    63
    """
    assert (symbol in BASE64_SYMBOLS), "decode_base64_symbol: the symbol is not part of base64"
    return BASE64_SYMBOLS.index(symbol)


#Question 8:
def symbols_to_bytes(symbols):
    """
    Convert base64 symbols to bytes

    :param symbol: A  string of four base64 symbols (and maybe the = sign)
    :type symbol: str
    :return: A list of one to 3 bytes whose values correspond to the base64 symbols
    :rtype: list
    :CU: len(symbols) == 4

    :Examples:
    >>> symbols_to_bytes('BQ==')
    [5]
    >>> symbols_to_bytes('BKM=')
    [4, 163]
    >>> symbols_to_bytes('HFll')
    [28, 89, 101]
    """
    assert (len(symbols) == 4), "The lenght of the string is inferior or equal to 4"
    b=''
    for symb in symbols:
        if symb!="=":
            sy=bin(int(decode_base64_symbol(symb)))[2:]
            while len(sy)<6:
                sy='0'+sy
            b+=sy
    l=[]
    while len(b)!=0:
        l.append(int(b[:8],2))
        b=b[8:]
    if l[len(l)-1]==0:
        l=l[:len(l)-1]
    return l


#Question 9:
def process_base64_line(line):
    """
    Process a line from a base64 input and writes the conversion on the output

    :param line: line of a base64 output
    :type line: str
    :CU: len(line) % 4 == 0 and the line only contains base64 symbols (or possibly = signs)
    """
    assert (type(line)==str),"Line must be a str"
    assert (len(line)%4 == 0), "Line must be a multiple of 4"
    l=[]
    for i in range(0,len(line),4):
        l+=symbols_to_bytes(line[i:i+4])
    conv=''
    for nbr in l:
        conv+=chr(int(nbr))
    return conv

        
#Question 10:
def base64_decode(source):
    """
    Decode a source file encoded in base64 and output the result.

    :param source: The filename of the base64 file to decode
    :type source: str
    """
    input = open(source, 'rb')
    lines = input.readlines()
    l=''
    for line in lines:
        l+=process_base64_line(str(line)[2:len(line)+1])
    input.close()
    j=0
    for i in range(len(l)-1):
        if (l[i+1]=="\n"):
            print (l[j:i+1],end='')
            j=i+1
