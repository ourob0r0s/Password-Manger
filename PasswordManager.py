import secrets
import string
import sqlite3
import pyperclip as pc

conn = sqlite3.connect('Database')
cursor = conn.cursor()
try:
    table = """CREATE TABLE PASSKEEP(
            NAME VARCHAR(100) NOT NULL,
            PASS VARCHAR(100) NOT NULL,
            PRIMARY KEY(NAME)
            );"""

    cursor.execute(table)
except Exception as e:
    print(e)


def generatePassword(n):
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(n))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break

    return password


def generatePasswordPunc(n):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(n))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3) \
                and any(not c.isalnum() for c in password):
            break
    return password


def insert(name, passcode):
    conn = sqlite3.connect('Database')
    cursor = conn.cursor()

    insert_query = 'INSERT INTO PASSKEEP VALUES (\'' + name + '\', \'' + passcode + '\')'
    cursor.execute(insert_query)
    conn.commit()
    conn.close()


def readP(name):
    conn = sqlite3.connect('Database')
    c = conn.cursor()

    c.execute('SELECT PASS FROM PASSKEEP WHERE NAME = \'' + str(name) + '\'')

    passcode = c.fetchone()
    conn.close()
    if passcode is None:
        print("no enterie by this name")
        return
    return passcode


def readN():
    conn = sqlite3.connect('Database')
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    names = c.execute('SELECT NAME FROM PASSKEEP').fetchall()
    conn.close()
    return names



def main():
    print('-------------------------------')
    print('---Welcome to PasswordManger---')
    print('-------------------------------')

    choice = 0
    while True:
        try:
                print('1) all passwords')
                print('2) password by name')
                print('3) new entery')
                print('-1) exit')
                choice = int(input())
                if choice == 1:
                    names = readN()
                    for name in names:
                        print('name:  '+name )

                elif choice == 2:
                    name = input("enter the name")
                    password = str(readP(name))

                    if password is None:
                        pc.copy(password)

                elif choice == 3:
                    print('please enter name: ')
                    name = input()

                    while True:
                        try:
                            print('automaticly generated passwords')
                            print('1) with special characters')
                            print('2) no special characters')
                            print('3) custom')
                            c2 = int(input())
                            if c2 == 1:
                                password = generatePasswordPunc(25)
                                break
                            elif c2 == 2:
                                password = generatePassword(20)
                                break
                            elif c2 == 3:
                                password = input()
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            pass

                    insert(name, password)
                elif choice == -1:
                    break
        except ValueError:
                pass

main()