# testing with GHClogoSmall_b64_png.txt
file = input("What file would you like to decode?: ")
# is now: GHClogoSmall_b64_png.txt
file_clean = file.replace(".txt", "").replace("b64_", "")
# is now: GHClogoSmall_png (1 line solution to a 2 line problom 🤑)


print(file_clean)

# reads inputed file and places it into a veriable