# decrypt.py
# Decrypts a line of text using a Caesar cipher
# Works for all printable ASCII characters

code = input("Enter the encrypted text: ")
distance = int(input("Enter the distance value: "))

plainText = ""

for ch in code:
    if 32 <= ord(ch) <= 126:  # printable ASCII range
        shifted = (ord(ch) - 32 - distance) % 95
        plainChar = chr(shifted + 32)
        plainText += plainChar
    else:
        # Leave non-printable characters unchanged
        plainText += ch

print("Decrypted text:", plainText)
