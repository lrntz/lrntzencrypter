# lrntzencrypter
A simple encryption/decryption program for sending messages.

## How to use:

1. Generate code using `keygenerate.py`
    Simply run the program and it will prompt you to enter a number between 1 and 9, enter this number and press enter to generate a key-set.

2. Encrypt a message using `encrypt.py`
    The program will automatically load the key-set and prompt you to enter a message. This message can be both lower and uppercase, but will always be decrypted in uppercase letters. Do not use space or any special characters.

3. Decrypt the message using `decrypt.py`
    Run the program and it will prompt you to enter the encrypted code. The program will automatically load the key-set and decrypt the code when entered.