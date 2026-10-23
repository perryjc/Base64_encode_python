import base64

img_path = input("input image file path: ").strip("'/'")

def convert(image):
    #Opens the file in a way that rb can read it
    with open(image, "rb") as image_file:
        image_bytes = image_file.read() 
        # reads the bytes and returns it
        print(image_bytes)

data = convert(img_path)
print((data))

def base64conversion(data):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    bit_string = ""
    for byte in data: 
        bit_string ="".join(f"{b:08b}" for b in data)
        #converting the byte into 8-digit binary in a formatted string literal (f"") --> b = conversion to binary, 8 = 8 chars/digits, 0 = pad with leading zeros


#some bits dont divide into 6-bit chunks, which is why padding is needed here
    padding = 0
    #when divided, if there is a remainder, the if statement is used
    if len(bit_string) % 6 != 0:
        remainder = len(bit_string) % 6
        need_padding = 6 - remainder
        bit_string += "0" * padding_needed
        # Every 2 bits of padding added equals 1 '=' at the end
        padding = need_padding //2
    encoded = ""

    # grouped into 6-bit chunks
    for i in range(0, leng(bit_string), 6):
        six_bits = bit_string[i:i+6]
        index = int(six_bits, 2)
        encoded_str += b64_chars[index]
#replaces trailing characters with =
    if padding > 0:
        encoded_str = encoded.str[:-padding] + ("=" * padding)
        return encoded
print(f"Encoded {base64conversion(img_path)}")



#3 bytes = 24 bits --> 4 groups of 6 bits
#0 to 25: A - Z
# 26 to 51: a - z
# 52 to 61: 0 - 9
# 62: +
#63: /

