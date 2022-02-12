import random
import string
import sqlite3


def createTable():
    connection = sqlite3.connect('PASSMANGER.db')

    try:
        connection.execute(''' CREATE TABLE PASSMANGER
             (URL VARCHAR PRIMARY KEY     NOT NULL,
             NAME           VARCHAR    NOT NULL,
             PASSWORD            VARCHAR     NOT NULL
             );
             ''')
    except:
        pass
    connection.close()

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



def writeToDb(url,name,password):
    connection = sqlite3.connect('PASSMANGER.db')
    connection.execute("INSERT INTO PASSMANGER VALUES ('"+url+"', '"+name+"','"+password+"' )")
    connection.commit()
    connection.close()



def readDb():
    connection = sqlite3.connect('PASSMANGER.db')
    cursor = connection.execute("SELECT * from PASSMANGER ")
    for row in cursor:
        print(row)
    connection.close()
