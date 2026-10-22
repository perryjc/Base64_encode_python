# testing with GHClogoSmall_b64_png.txt
def b64_txt_file2og(b64_filename):
    file = b64_filename
    # is now: GHClogoSmall_b64_png.txt
    file_clean = file.replace(".txt", "").replace("b64_", "")
    # is now: GHClogoSmall_png (1 line solution to a 2 line problom 🤑)
    file_og = file_clean.split("_")
    # is now: ['GHClogoSmall', 'png']
    filename = file_og[0]
    filetype = "." + file_og[1]
    return filename + filetype
    # returns GHClogoSmall.png working!


print(b64_txt_file2og("GHClogoSmall_b64_png.txt"))

# reads inputed file and places it into a veriable