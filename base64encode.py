
img_path = input("input image file path: ").strip("'/'")

def convert(image):
    #Opens the file in a way that rb can read it
    with open(image, "rb") as image_file:
        image_bytes = image_file.read() 
        # reads the bytes and returns it
        print(image_bytes)

bytes_converted = convert(img_path)
print((bytes_converted))


new_file ="testfile1.txt"
imagebytes = open(new_file, 'wb')
imagebytes.write(bytes_converted)
imagebytes.close()
print(new_file)


#def base64conversion(data):
   # chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
   # for i in range(len(data)):
    #    converted_char  = data([i]
     #   index = base64_chars.index(converted_char)
      #  print(index)

#output = base64conversion(bytes_converted)
#print(output)





