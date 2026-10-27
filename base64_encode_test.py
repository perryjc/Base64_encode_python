
def encode(s):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_list = []
    for i in range(len(s)):
        char = s[i]
        index = base64_chars.index(char)
        base64_list.append(index)
    print(base64_list)

encode("W1sT/P")
encode("ABCDEFG")
encode("abcdefg")
encode("12345")
