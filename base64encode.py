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

    result = []
    i = 0
    bytelength = len(data)

    while i < bytelength:
        remaining = bytelength - i
        



# call the function and print it

#3 bytes = 24 bits --> 4 groups of 6 bits
#0 to 25: A - Z
# 26 to 51: a - z
# 52 to 61: 0 - 9
# 62: +
#63: /

