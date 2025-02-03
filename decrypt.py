import string
import json

def importkey() -> dict:
    f = open("key.txt", "r")
    charlist = json.loads(f.read())
    f.close()
    return charlist

def flipdictionary(src: dict) -> dict:
    dst = dict((v,k) for k,v in src.items())
    return dst

#Run import code, calculate codestrength, flip dictionary for decryption.
key = importkey()
codestrength = len(key['A'])
charlist = flipdictionary(key)

#Debug logging
print(charlist)
print(codestrength)

print(f"Codes assigned\n")
encryptedmessage = input(f"Enter encrypted message:\n")
decryptedmessage = ''

#print(charlist[encryptedmessage[:codestrength]])

for n in range(0, len(encryptedmessage), codestrength):
    decryptedmessage += charlist[encryptedmessage[n:n+codestrength]]

print(decryptedmessage)