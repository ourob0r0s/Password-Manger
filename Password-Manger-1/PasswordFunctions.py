import random
import string
import sqlite3

conn = sqlite3.connect('CCS227')
cursor = conn.cursor()
try:
    table = """CREATE TABLE PASSKEEP(
            NAME VARCHAR(100) NOT NULL,
            PASS VARCHAR(100) NOT NULL,
            PRIMARY KEY(NAME)
            );"""

    cursor.execute(table)
except Exception:
    pass

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

def insert(name, passw):
    conn = sqlite3.connect('CCS227')
    cursor = conn.cursor()
    'encrypt(passw)'

    insert_query = 'INSERT INTO PASSKEEP VALUES (\'' + name + '\', \'' + passw + '\')'
    cursor.execute(insert_query)
    conn.commit()
    conn.close()

def readP(name):
    conn = sqlite3.connect('CCS227')
    c = conn.cursor()
    c.execute('SELECT * FROM PASSKEEP WHERE NAME = \''+str(name)+'\'')
    passw = c.fetchone()
    'decrypt(passw)'
    conn.close()
    return passw[1]
        
def readN():
    conn = sqlite3.connect('CCS227')
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    names = c.execute('SELECT NAME FROM PASSKEEP').fetchall()
    conn.close()
    return names

'def genKey():'
   

'def encrypt():'
    

'def decrypt(key):'
    
