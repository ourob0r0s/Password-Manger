import PasswordFunctions as pf
import pyperclip as pc

print('-----------Welcome to PasswordManger-----------')

choice = 0
while True:
    try:
            print('----------------------')
            print('1) all passwords')
            print('2) password by name')
            print('3) new entery')
            print('-1) exit')
            choice = int(input())
            if choice == 1:
                names = pf.readN()
                for name in names:
                    print(name)
                    print("****")
            elif choice == 2:
                name = input("enter the name")
                pc.copy(str(pf.readP(name)))        
            elif choice == 3:
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

                pf.insert(name, password)
            elif choice == -1:
                break
    except ValueError:
            pass







