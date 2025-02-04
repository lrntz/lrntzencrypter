import random
import string
import json

def importkey():
    f = open("key.txt", "r")
    charlist = json.loads(f.read())
    f.close()
    return charlist

charlist = importkey()
codestrength = str(len(charlist['A']))
print(f'Codestrength detected: {codestrength}\n')

print(f"Codes assigned...\n")

rawmessage = input(f"Enter your message (Message can be typed in both upper and lowercase, but message will always be decrypted in uppercase.):\n\n")

print(f"Encrypting your message...\n")

encryptedmessage = ''

for n in rawmessage:
    encryptedmessage += str(charlist[n])

print(encryptedmessage)