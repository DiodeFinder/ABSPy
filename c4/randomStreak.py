#Generate Random coin flip and Count streak of 6
import random
numberOfStreaks = 0

def streakCount(list):
    global numberOfStreaks
    for i in range (len(list) - 6):
        steak = 0
        for steak in range(6):
            if (list[i] != list[i+1]):
                break
        if steak == 5:
             numberOfStreaks += 1

for experimnetNumber in range(1000):
    # create 100 h or t value
    list = []
    for i in range(100):
        toss = random.randint(0, 1)
        if toss == 0:
            data = 'H'
        else:
            data = 'T'
        list.append(data)
    #check the number of streak in it
    print(list)
    streakCount(list)


print('Chances of streak: %s%%' %(numberOfStreaks / 1000))
