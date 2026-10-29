def encode(s):
    """
      >>> encode("W1sT/P")
      [22, 53, 44, 19, 63, 15]
      >>> encode("ABCDEFG")
      [0, 1, 2, 3, 4, 5, 6, 7]
      >>> encode("abcdefg")
      [26, 27, 28, 29, 30, 31, 32]
      >>> encode("12345")
      [53, 54, 55, 56, 57]
      >>> result = encode("12345")
      >>> result
      [53, 54, 55, 56, 57]
    """
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_list = []
    for i in range(len(s)):
        char = s[i]
        index = base64_chars.index(char)
        base64_list.append(index)
    return base64_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()

def bits_to_base64(bitstr):
    """
    >>> bits_to_base64('010001110100100001100111')
      'R0hn'
>>> bits_to_base64('010101000110010101110011')
      'VGVz'
      >>> bits_to_base64('01001101')
      'TQ=='
      >>> bits_to_base64('0100110101100001')
      'TWE='
      >>> s = '100111010110100101010011010111100111011110001110110101110011011'
      >>> result = bits_to_base64(s)
      >>> result
      'nWlTXneO1zD'
      >>> s2 = '10110101100010110011010101010110111100011101101011100101'
      >>> result2 = bits_to_base64(s2)
      >>> result2
      'tYs1VvHa5Q=='
    """
    b64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    padding = 0
    while len(bitstr) % 6 != 0:
        bitstr += "0"
        padding += 1
    byte_padding = (6-(len(bitstr) // 6 * 6 - (len(bitstr) - padding_count)))//2
    extra_bits = (6-(len(bitstr) % 6)) % 6
    padded = bitstr + ('0' * extra_bits)

    encoded = []
    for i in range(0, len(padded), 6):
        chunk = padded[i:i+6]
        value = int(chunk, 2)
        encoded.append(b64_chars[value])

    pad_len = (4 - (len(encoded_chars) % 4)) % 4
    result = "".join(encoded_chars) + ("=" * pad_len)

    return result

if __name__ = "__main__":
    import doctest
    doctest.testmod()









