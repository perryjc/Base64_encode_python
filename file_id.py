# testing with GHClogoSmall_b64_png.txt
def b64_txt_file2og(b64_filename):
    file = b64_filename
    # is now: GHClogoSmall_b64_png.txt
    file_og = file.replace(".txt", "").replace("b64_", "").split("_")
    # is now: GHClogoSmall_png (1 line solution to a 3 line problom???)
    #   file_og = file_clean.split("_")
    # is now: ['GHClogoSmall', 'png']
    return file_og[0] + "." + file_og[1]
    #   filetype = "." + file_og[1]
    #   return filename + filetype
    #   returns GHClogoSmall.png working!


print(b64_txt_file2og("GHClogoSmall_b64_png.txt"))

# reads inputed file and places it into a veriable