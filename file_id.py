# testing with GHClogoSmall_b64_png.txt
file = input("What file would you like to decode?: ")
# is now: GHClogoSmall_b64_png.txt
file_clean = file.replace(".txt", "").replace("b64_", "")
# is now: GHClogoSmall_png (1 line solution to a 2 line problom 🤑)
file_og = file_clean.split("_")
# is now: ['GHClogoSmall', 'png']
filename = file_og[0]
filetype = "." + file_og[1]

output_file = filename + filetype
# returns GHClogoSmall.png working!


print(output_file)

# reads inputed file and places it into a veriable