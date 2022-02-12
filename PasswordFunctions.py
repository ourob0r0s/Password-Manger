import random
import string
# Fernet module is imported from the
# cryptography package
from cryptography.fernet import Fernet

special = '!"£$%^&*.,@#/?'
def generatePassword(n):
    password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + special) for _ in range(n))
    password = list(password)
    num = random.randint(0, n-1)
    taboo = []

    if password[num] is not string.ascii_uppercase:
       password[num] = random.SystemRandom().choice(string.ascii_uppercase)
    taboo.append(num)

    while num in taboo:
        num = random.randint(0, n-1)
    if password[num] is not string.ascii_lowercase:
       password[num] = random.SystemRandom().choice(string.ascii_lowercase)
    taboo.append(num)

    while num in taboo:
        num = random.randint(0, n-1)
    if password[num] is not string.digits:
       password[num] = random.SystemRandom().choice(string.digits)
    taboo.append(num)

    while num in taboo:
        num = random.randint(0, n-1)
    if password[num] is not special:
       password[num] = random.SystemRandom().choice(special)


    password = "".join(password)

    return password



def writeToFile(password):
    f = open("passwords.txt", "a")
    f.write(password+"\n")
    f.close()


def readFile():
    f = open("passwords.txt", "r")
    print(f.read())
    f.close()

def genKey():
    key = Fernet.generate_key()

    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)


def encrypt():
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open('passwords.txt', 'rb') as file:
        original = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open('password.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    return key

def decrypt(key):
    # using the key
    fernet = Fernet(key)

    # opening the encrypted file
    with open('password.txt', 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    with open('password.txt', 'wb') as dec_file:
        dec_file.write(decrypted)
