def decode(nums):
    """
      >>> decode([22, 53, 44, 19, 63, 15])
      'W1sT/P'
      >>> decode([0, 1, 2, 3, 4, 5, 6, 7])
      'ABCDEFG'
      >>> decode([26, 27, 28, 29, 30, 31, 32])
      'abcdefg'
      >>> decode([53, 54, 55, 56, 57])
      '12345'
    """
    b64char_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    b64char_list = list(b64char_str)
    output = ""

    for num in nums:
        char = b64char_list[num]
        output += char

    return output
