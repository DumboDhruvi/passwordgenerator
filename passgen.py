import random
import sys
import csv


def main():
    try:
        i = int(input('enter number of digits in password: '))
    except ValueError:
        sys.exit('Wrong value type entered')
    if len(sys.argv) > 1:
        keyword = sys.argv[1]
    else:
        keyword = 'abcdefghijklmopABCDEFGHIJKLMOPZ123456789+-/%&'
    password = genetaror(keyword, i)
    print(password)
    name = input('input the name of your password: ')
    S = storage(password, name)
    print(S)
    files(S)


def genetaror(keyword, i):
    a = ''
    for n in range(i):
        a += (random.choice(keyword))
    return a


def storage(password, name):
    stor = {}
    stor.update({'name': name, 'password': password})
    return stor


def files(s):
    stor = [s]

    with open('pass.csv', 'r') as _pass:
        old_pass = csv.DictReader(_pass)
        for i in old_pass:
            stor.append(i)
    print(stor)

    with open('pass.csv', 'w', newline='') as password:
        fields = ['name', 'password']
        password = csv.DictWriter(password, fieldnames=fields)
        password.writeheader()
        for i in range(len(stor)):
            password.writerow(stor[i])


main()
