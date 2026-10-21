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

# call the function and print it
# 10/21, says that the file link doesn't work FIX IT !!
