import random
import string
import json

#The function that assigns codes to characters
codestrength = int(input(f"How strong do you want the encryption to be? (Minimum of 2)\n\n"))

def makechar(codestrength):
    character = random.choice(string.digits)

    for n in range(codestrength - 1):
        character += random.choice(string.digits)
    
    return character

#Assign code to each letter of the alphabet
charlist = {}
for c in string.ascii_uppercase + string.ascii_lowercase + " " + "?" + "!":
    charlist[c] = makechar(codestrength)

print(f'Generated codes: \n\n{charlist}')

f = open("key.txt", "w")
f.write(json.dumps(charlist))
f.close()