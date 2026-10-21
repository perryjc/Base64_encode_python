import sys
import base64

file = input("What file would you like to decode?: ")

# reads inputed file and places it into a veriable
f = open(file)
encoded_txt = f.read()

# photo_bytes = base64.b64decode(encoded_txt)
# this fuction does the same thing as base64.b64decode without having to import a module
def b64decode(bytes_to_decode):

    base64char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    char_map = {}
    # Indexes the charset of the 64 Base64 characters and creates a fast lookup table. 
    for index, char in enumerate(base64char):
        char_map[char] = index

    # math mismatch/bit loss solution
    bit_buffer = 0
    bits_count = 0
    decoded_bytes = bytearray()

    for char in bytes_to_decode:
        if char in char_map:
            bit_buffer = (bit_buffer << 6) | char_map[char]
            bits_count += 6

            if bits_count >= 8:
                bits_count -= 8
                decoded_bytes.append((bit_buffer >> bits_count) & 0xFF)
    return bytes(decoded_bytes)

photo_bytes = b64decode(encoded_txt)

# creates and opens new png file
imagebytes = open('GHClogoSmall_test.png', 'wb')
# writes the bytes to the new file
imagebytes.write(photo_bytes)
# closes file
imagebytes.close()


print("Finshed! The decoded image is named GHClogoSmall_test.png")
