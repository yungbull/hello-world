plainText = input("Enter a message: ")
distance = int(input("Enter the distance value: "))

code = ""

for ch in plainText:
    if 32 <= ord(ch) <= 126:  # printable ASCII range
        shifted = (ord(ch) - 32 + distance) % 95
        cipherChar = chr(shifted + 32)
        code += cipherChar
    else:
        
        code += ch

print("Encrypted text:", code)
