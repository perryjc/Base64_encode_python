import sys
import base64

file = input("What file would you like to decode?: ")

# reads inputed file and places it into a veriable
f = open(file)
encoded_txt = f.read()

bytes_decoded = base64.b64decode(encoded_txt)

# creates and opens new png file
imagebytes = open('GHClogoSmall_test.png', 'wb')
# writes the bytes to the new file
imagebytes.write(bytes_decoded)
#closes file
imagebytes.close()

print("Finshed! The decoded image is named GHClogoSmall_test.png")
