#encrypt and decrypt cipher texts with the ceasar cipher

from sys import argv, exit
#working with upper case letters on the ascii table from 65 to 90
def encrypt(text, key, start=65, end=90):
    encrypted = []
    for letter in text:
        #shifting the letter by the key value
        asci = ord(letter) + key
        #checking if the new ascii code is past the uppercase letters 
        if asci > end:
            new_key = asci - end
            asci = start  + new_key - 1
        encrypted.append(chr(asci))
    return "".join(encrypted)

def decrypt(text, key, start=65, end=90):
    decrypted = []
    for letter in text:
        asci = ord(letter) - key
        if asci < start:
            new_key = start - asci
            asci = end - new_key + 1
        decrypted.append(chr(asci))
    return "".join(decrypted)
 

if __name__ == "__main__":
    if len(argv) != 4:
        print(f"usage :python3 {__file__} text key -e|-d (encrypt/decrypt)")
        exit()
    
    text = argv[1].upper()
    key = int(argv[2])
    option = argv[3]
    
    if option == "-e":
        print(encrypt(text, key))
    else:
        print(decrypt(text, key))

       
