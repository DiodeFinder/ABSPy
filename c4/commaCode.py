def commaCode(list):
    countNumber = 0
    joined = ''
    while countNumber < len(list) - 2:
        joined += list[countNumber] + ', '
        countNumber += 1
    joined += list[-2] + ' and '
    joined += list[-1] + '.'
    return joined

list = []
count = 1
print("Please enter your list of item to convert into a sentence, input s to stop.")
while True:
    print('(',count,')', end = ' ')
    data = str(input())
    if data == 's':
        break
    else:
        list.append(data)
        count += 1

print('ORIGINAL LIST : ',list)   
try:
    print('YOUR RESULT : ',commaCode(list))
except:
    print("You need to enter minimum 2 data to get result.")
