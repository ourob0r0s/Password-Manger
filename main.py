import PasswordFunctions

print('-----------Welcome to PasswordManger-----------')
print('please enter username: ')
username = input()
print('please enter password: ')
password = input()
choice = 0
while choice != -1:
    print('----------------------')
    print('1) all passwords')
    print('2) password by name')
    print('3) password by url')
    print('-1) exit')
    choice = int(input())

    if choice == 1:
        PasswordFunctions.readDb()
    elif choice == 2:
        print()
    elif choice == 3:
        print()
    elif choice == -1:
        quit()


