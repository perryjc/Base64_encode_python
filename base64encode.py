
img_path = input("input image file path: ").strip("'/'")

def convert(image):
    #Opens the file in a way that rb can read it
    with open(image, "rb") as image_file:
        image_bytes = image_file.read() 
        # reads the bytes and returns it
    bitstr = ""
    for byte in image_bytes:
        for place in range(7, -1, -1):
            if byte & ( 1 << place):
                bitstr += '1'
            else:
                bitstr += '0'
    return bitstr


bytes_converted = convert(img_path)

def base64_conversion(data):
    chars = "ABCDEFGHIJKLMNOPQRSTUVQXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    b64_string = ""
    total_bytes = len(data)//8
    rem_bytes = total_bytes % 3

    while len(data) % 6 != 0:
        data += "0"
    for i in range(0, len(data), 6):
        six_bits = data[i:i+6]
        index = int(six_bits,2)
        b64_string += chars[index]
    if rem_bytes == 1:
        b64_string += "=="
    elif rem_bytes == 2:
        b64_string += "="
    return b64_string




b64converted = base64_conversion(bytes_converted)

output_file = "testfile1.txt"
with open(output_file, "w", encoding = "utf-8") as file:
    file.write(b64converted)




