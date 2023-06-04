# rail fence cipher

plaintext = input("Type a message to encode: ")
plaintext = plaintext.upper()
plaintext = plaintext.replace(" ", "")

top = ""
bottom = ""
i = 0

for ch in plaintext:
    if i % 2 == 0:
        top += ch
    else:
        bottom += ch
    i += 1

cipher = top + bottom
print(cipher)
