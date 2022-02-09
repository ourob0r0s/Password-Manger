import random
import string
special = '!"£$%^&*.,@#/?'
def generatePassword():
    password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + special) for _ in range(14))
    return password

