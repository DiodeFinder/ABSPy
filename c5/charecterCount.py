message = 'It was bright cold day in april, and the clocks striking thirteen'
count = {}

for charecter in message:
	count.setdefault(charecter, 0)
	count[charecter] = count[charecter] + 1

print('count = ',count)