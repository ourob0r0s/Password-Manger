import PasswordFunctions as pf
import getpass
database = {"admin": "admin"}



print('-----------Welcome to PasswordManger-----------')

username = 0
password = 0
for i in database.keys():
    while username != i and password != database.get(i):
        print('please enter username: ')
        username = input()
        print('please enter password: ')
        password = input()
        if username == i and password == database.get(i):
            break
        print("username or password incorrect ")
        print("------------------------------\n")



print("Verified")







choice = 0
while True:
    try:
            print('----------------------')
            print('1) all passwords')
            print('2) password by name')
            print('3) password by url')
            print('4) new entery')
            print('-1) exit')
            choice = int(input())
            if choice == 1:
                pf.readDb()
            elif choice == 2:
                print()
            elif choice == 3:
                print()
            elif choice == 4:
                print('please enter url: ')
                url = input()
                print('please enter name: ')
                name = input()

                while True:
                    try:
                        print('automaticly generated passwords')
                        print('1) Very Strong')
                        print('2) Strong')
                        print('3) Medium')
                        print('4) easy')
                        c2 = int(input())
                        if c2 == 1:
                            password = pf.generatePassword(25)
                            break
                        elif c2 == 2:
                            password = pf.generatePassword(20)
                            break
                        elif c2 == 3:
                            password = pf.generatePassword(14)
                            break
                        elif c2 == 4:
                            password = pf.generatePassword(8)
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        pass

                pf.writeToDb(url, name, password)
            elif choice == -1:
                break
    except ValueError:
            pass







