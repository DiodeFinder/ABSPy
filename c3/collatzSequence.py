import sys

def collatz(number):
    if (number%2) == 0 :
        number = number // 2
    else:
        number = 3 * number + 1
    return int(number)

try:
    number = 0
    getBack = 0
    print('The Collatz Sequence')
    while True:
        print('Enter a Number: ')
        number = int(input())
        getBack = collatz(number)
        while not(getBack == 1):
            print(getBack)
            getBack = collatz(getBack)

except KeyboardInterrupt:
    sys.exit()
