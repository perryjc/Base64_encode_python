
def encode(s):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for s in input_chars:
        if s in base64_chars:
            index = base64_chars.index(s)
            print(f"{index}")
        elif char == "=":
            print(f"Padding")
        else:
            print("Not Valid")


