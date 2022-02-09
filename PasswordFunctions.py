import random
import string
special = '!"£$%^&*.,@#/?'
def generatePassword():
    password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + special) for _ in range(14))
    password = list(password)
    num = random.randint(0, 13)
    taboo = []

    if password[num] is not string.ascii_uppercase:
       password[num] = random.SystemRandom().choice(string.ascii_uppercase)
    taboo.append(num)

    while num in taboo:
        num = random.randint(0, 13)
    if password[num] is not string.ascii_lowercase:
       password[num] = random.SystemRandom().choice(string.ascii_lowercase)
    taboo.append(num)

    while num in taboo:
        num = random.randint(0, 13)
    if password[num] is not string.digits:
       password[num] = random.SystemRandom().choice(string.digits)
    taboo.append(num)

    while num in taboo:
        num = random.randint(0, 13)
    if password[num] is not special:
       password[num] = random.SystemRandom().choice(special)


    password = "".join(password)

    return password


def writeToFile(password):
    f = open("Passwords.txt", "a")
    f.write(password+"\n")
    f.close()


def readFile():
    f = open("passwords.txt", "r")
    print(f.read())
    f.close()
