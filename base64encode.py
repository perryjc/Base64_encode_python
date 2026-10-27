import base64

img_path = input("input image file path: ").strip("'/'")

def convert(image):
    #Opens the file in a way that rb can read it
    with open(image, "rb") as image_file:
        image_bytes = image_file.read() 
        # reads the bytes and returns it
        print(image_bytes)

bytes_converted = convert(img_path)
print((bytes_converted))

def base64conversion(data):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for i in range(len(data)):
        converted_char  = data[i]
        index = base64_chars.index(converted_char)
        print(index)

base64conversion(bytes_converted)
