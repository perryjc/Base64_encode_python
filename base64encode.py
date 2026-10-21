import base64

img_path = input("input image file path: ")

def acceptimage(image):
    img_path = img_path.strip("'/'")
    #strip quotes if the user dragged-->dropped file
    with open(img_path, "rb") as file:
        data = file.read()
        bytes = data[:10] 




acceptimage(img)
