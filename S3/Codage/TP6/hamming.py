import numpy as np

g_8_4 = np.matrix('1 0 0 0 1 1 0 1; 0 1 0 0 0 1 1 1; 0 0 1 0 1 0 1 1; 0 0 0 1 1 1 1 0')

controlT_g_8_4 = np.vstack([g_8_4.T[4:].T, np.identity(4, dtype=int)])
modulo2 = np.vectorize(lambda i: i % 2)


def value_to_vector(value, size):
    '''
    Transform an integer to a vector of the given size.

    :param value: The integer to transform in a binary vector
    :type value: int
    :param size: The size of the returned vector
    :type size: int
    :return: A matrix of 1 row and `size` elements. The elements in the matrix\
    correspond to the base 2 representation of the integer.
    :rtype: matrix
    :UC: 0 <= value < 2^size
    :Examples:

    >>> np.array_equal(value_to_vector(0, 4), np.matrix('0 0 0 0'))
    True
    >>> np.array_equal(value_to_vector(12, 4), np.matrix('1 1 0 0'))
    True
    >>> np.array_equal(value_to_vector(13, 4), np.matrix('1 1 0 1'))
    True
    '''
    assert value >= 0 and value < (1 << size), "The value cannot fit in %d bits" % size
    binary_list = [int(i) for i in ('{0:0%db}' % size).format(value)]
    return np.matrix(binary_list)

def vector_to_value(vector):
    '''
    Transform a vector to an integer

    :param vector: A binary matrix containing a single row
    :type vector: matrix
    :return: The inverse of the function `hamming.value_to_vector`
    :rtype: int
    :Examples:

    >>> vector_to_value(np.matrix([1, 0, 0, 0]))
    8
    >>> vector_to_value(value_to_vector(12, 4))
    12
    >>> vector_to_value(value_to_vector(0, 4))
    0
    '''
    binary_list = vector.tolist()[0]
    n = len(binary_list)
    return sum(b << (n-i-1) for i, b in enumerate(binary_list))


def hamming_encode(value, g):
    '''
    For a Hamming (or Hamming-like) encoding taking 4 bits in input.

    :Param value: An integer value where at most the four least significant bits are set
    :Type value: int
    :Param g: The generating matrix for that encoding
    :Type g: matrix
    :Return: The value of the Hamming encoding using the generating matrix g.
    :Rtype: int
    :UC: 0 <= value < 16
    :Examples:
    >>> hamming_encode(0, g_8_4)
    0
    >>> hamming_encode(0b1101, g_8_4) == 0b11010100
    True
    '''
    assert (0 <= value < 16), "value must be between 0(included) and 16 (excluded)"
    return (vector_to_value(modulo2(value_to_vector(value, 4)*g_8_4)))


def encode_byte_8_4(byte):
    '''
    Encode the byte using Hamming-like [8,4] encoding

    :Param byte: The byte to encode
    :Type byte: int
    :Return: A list of two bytes corresponding to the encoding of byte
    :Rtype: list
    :UC: 0 <= byte < 256
    :Examples:
    >>> encode_byte_8_4(0b10100111) == [0b10100110, 0b01110010]
    True
    >>> encode_byte_8_4(0) == [0, 0]
    True
    '''
    assert (0<=byte<256), "Byte must be between 0(included) and 256 (excluded)"
    return [hamming_encode(byte >> 4, g_8_4), hamming_encode(byte & 0b00001111, g_8_4)]


def get_data_from_8_4(value, controlT):
    '''
    :Param value: A byte that was encoded using a [8, 4, 4]-linear coding
    :Type value: int
    :Param controlT:  The transpose of the control matrix of the encoding
    :Type controlT: matrix
    :Return: A tuple of three elements.
             1. The decoded value (between 0 and 16) using the [8, 4, 4]-linear coding. Errors are corrected, if possible.
             2. A boolean whose value is False iff no error was detected.
             3. A boolean whose value is False iff no error was corrected.
    :Rtype: tuple
    :UC: 0 <= value < 256
    :Examples:
    >>> get_data_from_8_4(0b01000111, controlT_g_8_4)
    (4, False, False)
    >>> get_data_from_8_4(0b01100111, controlT_g_8_4)
    (4, True, True)
    >>> get_data_from_8_4(0, controlT_g_8_4)
    (0, False, False)
    >>> get_data_from_8_4(4, controlT_g_8_4)
    (0, True, True)
    >>> get_data_from_8_4(0b01110111, controlT_g_8_4)
    (7, True, False)
    '''
    assert (0<=value<256), "value must be between 0(included) and 256 (excluded)"
    decod = modulo2(value_to_vector(value, 8) * controlT)
    if decod.tolist()[0]==[0, 0, 0, 0]:
        return(value>>4, False, False)
    else:
        i=0
        while (i<8) and (controlT.tolist()[i]!=decod.tolist()[0]) :
            i+=1
        if i<8:
            e=2**(7-i)
            return(int((value^e)>>4), True, True)
        else:
            return(value>>4, True, False)


def decode_byte_8_4(bytes_read):
    '''
    Using the two bytes that have been transmitted return the decoded byte (possibly corrected), together with information on the number of errors detected or corrected.

    :Param bytes_read: Two bytes
    :Type bytes_read: bytes
    :Return: A tuple of three elements.
             1. The decoded value (between 0 and 255) using the [8, 4, 4]-linear coding. Errors are corrected, if possible.
             2. An integer corresponding to the number of detected errors.
             3. An integer corresponding to the number of corrected errors.
    :Rtype: tuple
    :UC: len(bytes_read) == 2
    :Examples:
    >>> decode_byte_8_4(bytes([32, 128]))
    (0, 2, 2)
    >>> decode_byte_8_4(bytes([0b10100110, 0b01110010])) == (0b10100111, 0, 0)
    True
    >>> decode_byte_8_4(bytes([0b10100110, 0b01010010])) == (0b10100111, 1, 1)
    True    
    >>> decode_byte_8_4(bytes([0b11100110, 0b01010010])) == (0b10100111, 2, 2)
    True    
    >>> decode_byte_8_4(bytes([0b10110110, 0b01010010])) == (0b10100111, 2, 2)
    True    
    >>> decode_byte_8_4(bytes([0b11110110, 0b01010010])) == (0b11110111, 3, 1)
    True
    >>> decode_byte_8_4(bytes([0b11110110, 0b01110010])) == (0b11110111, 2, 0)
    True
    '''
    assert (len(bytes_read) == 2), "bytes_read must have a length of 2"
    data1=get_data_from_8_4(bytes_read[0], controlT_g_8_4)
    data2=get_data_from_8_4(bytes_read[1], controlT_g_8_4)
    detec_error=0
    correc_error=0
    if data1[1]==True:
        detec_error+=1
        if data1[2]==True:
            correc_error+=1
        else:
            detec_error+=1
    if data2[1]==True:
        detec_error+=1
        if data2[2]==True:
            correc_error+=1
        else:
            detec_error+=1
    value=data1[0]<<4 | data2[0]
    return(value, detec_error, correc_error)
