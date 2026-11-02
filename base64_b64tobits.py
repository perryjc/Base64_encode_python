def base64_to_bits(b64str):
    """
    >>> base64_to_bits('Rohn')
    '010001110100100001100111'
      >>> base64_to_bits('VGVz')
      '010101000110010101110011'
      >>> base64_to_bits('TQ==')
      '01001101'
      >>> base64_to_bits('TWE=')
      '0100110101100001'
      >>> base64_to_bits('nWlTXneO1zD')
      '100111010110100101010011010111100111011110001110110101110011000011'
      >>> s2 = '10110101100010110011010101010110111100011101101011100101'
      >>> base64_to_bits('tYs1VvHa5Q==') == s2
      True
    """
    result = ""
    bit_string = ""
    padding = len(b64str % 6 )
    if rem:
        b64str += "0" * (6 - padding)
    b64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for i in range(0, len(b64str), 6):
        bits = b64str[i:i+6]
        value = int(bits, 2)
        result += b64_chars[value]

    pad_rem = len(result) % 4
    if pad_rem:
        result += "=" * (4-pad_rem)
    return result



if __name__ == '__main__':
    import doctest
    doctest.testmod()

