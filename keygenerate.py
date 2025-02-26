import random
import string
import json

codestrength = 0

while codestrength < 2:
    #The function that assigns codes to characters
    codestrength = int(input(f"\nHow strong do you want the encryption to be? (Minimum of 2)\n\n"))

def makechar(codestrength):
    character = random.choice(string.digits)

    for n in range(codestrength - 1):
        character += random.choice(string.digits)
    
    return character

#Assign code to each letter of the alphabet
charlist = {}
for c in string.ascii_uppercase + string.ascii_lowercase + " æøåÆØÅ?!%":
    charcode = ''
    while charcode == '' or charcode in charlist.values():
        charcode = makechar(codestrength)
    charlist[c] = charcode

print(f'Generated codes: \n\n{charlist}')

f = open("key.txt", "w")
f.write(json.dumps(charlist))
f.close()