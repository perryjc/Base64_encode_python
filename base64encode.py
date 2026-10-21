import base64

img_path = input("input image file path: ").strip("'/'")

def convert(image):
    #Opens the file in a way that rb can read it
    with open(image, "rb") as image_file:
        image_bytes = image_file.read() 
        # reads the bytes and returns it
        return image_bytes
    base64 = base65.b64encode(image_bytes).decode("utf-8")
    print(base64)
    return base64
    #used the imported base64 module to conver the bytes to base64

data = convert(img_path)
print((data))

# call the function and print it
