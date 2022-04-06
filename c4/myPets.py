myPets = ['Caesar', 'Kai', 'Birdy']
print('Enter a pet name: ')
name = input()
if name not in myPets:
    print("I don't have a pet name "+name)
else:
    print(name + ' is my pet.')
    
