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
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    padding = (6 - len(bit_string) %6) % 6
    bit_string += "0" * padding_needed
    b64_result = ""
    for i in range(0, len(bit_string), 6):
        chunk = bit_string[i:i+6]
        val = int(chunk,2)
        result += alphabet[val]
    result += "=" * (padding_needed//2)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

