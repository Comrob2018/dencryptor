from pyAesCrypt import encryptFile, decryptFile
from random import randint
import os

keychars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ00112233445566778899'
buffersize = 64*2048

def encryptor():
    getfile = input("Please enter the name of the file: ")
    password = ''
    for i in range(0, 20):
        password += keychars[randint(0, 45)]
    print("Here is your encryption key: " + password + "\nPlease save this password.")
    encryptedfile = getfile + ".aes"
    encryptFile(getfile, encryptedfile, password, buffersize)
    os.rename(getfile, "."+getfile)
    print("Your file has been encrypted as " + encryptedfile + '.')
    
def decryptor():
    getfile = input("Please enter the name of the encrypted file: ")
    password = input("Please enter the key used to encrypt the file: ")
    decryptedfile = "decryptedfile.txt"
    decryptFile(getfile, decryptedfile, password, buffersize)
    print("Your file has been decrypted as " + decryptedfile + '.')
    
def dencryptor():
    encrypt = input("Would you like to encrypt a file? y/n ")
    if 'y' in encrypt:
        encryptor()
    elif 'n' in encrypt:
        decrypt = input("Would you like to decrypt a file? y/n ")
        if 'y' in decrypt:
            decryptor()
            
if __name__ == "__main__":
    dencryptor()
