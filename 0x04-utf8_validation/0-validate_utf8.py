#!/usr/bin/python3
"""UTF8 validator module
"""


def validUTF8(data):
    """UTF-8 validator
    Args:
        data: list of integers
    Return:
        True if data is a valid UTF-8  encoding,
        else return False
    """
    def countLeadingOnes(byte):
        """Count the number of leading 1s in the byte
        """
        mask = 1 << 7
        count = 0
        while byte & mask:
            count += 1
            mask >>= 1
        return count

    def isValidSequence(bytes):
        """Check if the sequence of bytes is a valid UTF-8 character
        """
        if len(bytes) == 1 or len(bytes) > 4:
            return False
        leadingOnes = countLeadingOnes(bytes[0])
        if leadingOnes < 2 or leadingOnes > 4 or leadingOnes != len(bytes):
            return False
        for i in range(1, len(bytes)):
            if countLeadingOnes(bytes[i]) != 1:
                return False
        return True

    i = 0
    while i < len(data):
        leadingOnes = countLeadingOnes(data[i])
        if leadingOnes == 0:
            i += 1
            continue
        if leadingOnes == 1 or leadingOnes > 4:
            return False
        sequence = data[i:i + leadingOnes]
        if not isValidSequence(sequence):
            return False
        i += leadingOnes

    return True
