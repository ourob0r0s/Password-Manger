import PasswordFunctions as pf
import pyperclip as pc

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
                names = pf.readN()
                for name in names:
                    print('name:  '+name )

            elif choice == 2:
                name = input("enter the name")
                password = str(pf.readP(name))

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
                            password = pf.generatePasswordPunc(25)
                            break
                        elif c2 == 2:
                            password = pf.generatePassword(20)
                            break
                        elif c2 == 3:
                            password = input()
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







