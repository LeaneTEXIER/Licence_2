def encode(byte):
    '''
    Encode the byte using repetition coding
    
    :Param byte: The byte to encode
    :Type byte: int
    :Returns: A list of three bytes equal to byte
    :Rtype: list
    :UC: 0 <= byte < 256
    :Examples:
    >>> encode(123)
    [123, 123, 123]
    >>> encode(0)
    [0, 0, 0]
    '''
    assert (0<=byte<256), "Byte must be between 0(included) and 256 (excluded)"
    return [byte, byte, byte]


def majority(bytes_read):
    '''
    :Param bytes_read: Three bytes
    :Type bytes_read: bytes
    :Returns: The returned byte is constituted of the majoritarian bits among the three bytes
    :Rtype: int
    :UC: len(bytes_read) == 3
    :Examples:
    >>> majority(bytes([0b00100001, 0b10100011, 0b10000000])) == 0b10100001
    True
    >>> majority(bytes([0b00000000, 0b10101010, 0b01101101])) == 0b00101000
    True
    '''
    assert (len(bytes_read) == 3), "bytes_read must have a length of 3"
    return (bytes_read[0]&bytes_read[1])|(bytes_read[0]&bytes_read[2])|(bytes_read[1]&bytes_read[2])


def binary_weight(w):
    '''
    :Param w: A number
    :Type w: int
    :Returns: The binary weight (ie. the number of 1 in the binary representation of w)
    :Rtype: int
    :Examples:
    >>> binary_weight(1)
    1
    >>> binary_weight(0)
    0
    >>> binary_weight(2)
    1
    >>> binary_weight(5)
    2
    >>> binary_weight(2048)
    1
    '''
    nb_1=0
    for b in bin(w):
        if b=='1':
            nb_1+=1
    return nb_1


def nb_errors(bytes_read):
    '''
    :Param bytes_read: Three bytes
    :Type bytes_read: bytes
    :Returns: The total number of errors among the bytes in bytes_read That corresponds to the number of positions where bits differ among the three bytes
    :Rtype: int
    :UC: len(bytes_read) == 3
    :Examples:
    >>> nb_errors(bytes([0b01, 0b10, 0b11]))
    2
    >>> nb_errors(bytes([0b0011100, 0b0010111, 0b1001000]))
    6
    '''
    assert (len(bytes_read) == 3), "bytes_read must have a length of 3"
    return (binary_weight(~(bytes_read[0]&bytes_read[1]&bytes_read[2])^(~bytes_read[0]&~bytes_read[1]&~bytes_read[2])))


def decode(bytes_read):
    '''
    Takes three bytes (encoded with repetition three times) and return a byte plus some information on the number of errors
    
    :Param bytes_read: Three bytes
    :Type bytes_read: bytes
    :Returns: A tuple whose first component is the byte made by looking at each position in the three bytes what bit is in majority, the second component is the number of detected errrors, and the last component is the number of corrected errors (both numbers are equal here).
    :Rtype: tuple
    :UC: len(bytes_read) == 3
    :Examples:
    >>> decode(bytes([0b00100001, 0b10100011, 0b10000000])) == (0b10100001, 4, 4)
    True
    '''
    assert (len(bytes_read) == 3), "bytes_read must have a length of 3"
    return (majority(bytes_read), nb_errors(bytes_read), nb_errors(bytes_read))
