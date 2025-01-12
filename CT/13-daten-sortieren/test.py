print(chr(97))
alphabet = []
for x in range(26):
    alphabet.append(chr(97+x))
print(alphabet)

for x in ("Lydia"):
    print(chr(ord(x.lower())))

print(chr(ord("lydia".lower())))