
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
bytes_object = bytes_converted.encode("utf-8")
print(bytes_object)

def base64_conversion(data):
    chars = "ABCDEFGHIJKLMNOPQRSTUVQXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    b64_string = ""
    for i in range(len(data)):
        converted_char = str(data[i])
        index = chars.index(converted_char)
        b64_string += str(index)
    return b64_string
b64converted = base64_conversion(bytes_converted)
print(b64converted)

with open("testfile1.txt", "w", encoding = "utf-8") as file:
    file.write(b64converted)
new_file = "testfile1.txt"
read = open("testfile1.txt", 'w')
read.write(b64converted)
read.close()
print(new_file)







