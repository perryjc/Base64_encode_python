import sys

# ASCII art on load
# DONT TOUCH THIS WAS DIFFICULT TO FIGURE OUT (thank you stackoverflow <3)
print(r"""
        ____  _____ __ __     ____                      __   
       / __ )/ ___// // /    / __ \___  _________  ____/ /__ 
      / __  / __ \/ // /_   / / / / _ \/ ___/ __ \/ __  / _ \
     / /_/ / /_/ /__  __/  / /_/ /  __/ /__/ /_/ / /_/ /  __/
    /_____/\____/  /_/    /_____/\___/\___/\____/\__,_/\___/                                                  
    """)
# link to ascii tool: https://patorjk.com/software/taag/#p=display&f=Slant&t=B64%20Decode%0A&x=none 

# allows the file to be called when lauching the script or as an input
try:
    file = sys.argv[1]
except IndexError:
    file = input("Enter name of the file you would like to decode (hit enter to exit): ")
    # if input is empty or nothing, script ends early, otherwise it continues
    if(file == "" or not file):
        sys.exit()
    else:
        print("Decodeing file")


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

def b64_txt_file2og(b64_filename):
    # see "file_id.py" for the line by line
    file = b64_filename
    file_og = file.replace(".txt", "").replace("_b64_", "$").split("$")
    return file_og[0] + "." + file_og[1]

photo_bytes = b64decode(encoded_txt)
new_file = b64_txt_file2og(file)

# creates and opens new png file
imagebytes = open(new_file, 'wb')
# writes the bytes to the new file
imagebytes.write(photo_bytes)
# closes file
imagebytes.close()


print("Finshed! The decoded file is named" + new_file)
