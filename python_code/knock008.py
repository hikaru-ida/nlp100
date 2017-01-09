def cipher(string):
    cip = ""
    for char in string:
        if char.islower():
            cip += chr(219-ord(char))
        else:
            cip += char
    return cip

if __name__ == '__main__':
    s = "aAbBcCdD"
    print(cipher(s))
