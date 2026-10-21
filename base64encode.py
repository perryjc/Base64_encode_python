import base64

img_path = input("input image file path: ").strip()

def convert(image):
    with open(image, "rb") as image_file:
        image_bytes = image_file.read() 
        return image_bytes
    base64 = base65.b64encode(bytes).decode("utf-8")
    print(base64)
    return base64

data = convert(img_path)
print((data))
