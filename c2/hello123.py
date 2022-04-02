# Write code that prints Hello if 1 is stored in spam , prints Howdy if 2 is stored in spam , and prints Greetings! if
# anything else is stored in spam .
import sys
spam = 0
while True:
	print('Enter spam value(1, 2, 3): ')
	try:
		spam = int(input())
	except:
		print('Only 1, 2, 3 and 4')
	if spam == 1:
		print('Hello')
	elif spam == 2:
		print('Howdy')
	elif spam == 3:
		print('Greetings !')
	elif spam == 4:
		sys.exit()
	else:
		continue

