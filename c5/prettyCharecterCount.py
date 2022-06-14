import pprint
message = "It was a bright cold day in April, and the clock were striking thirteen."
count = {}

for charecter in message:
   count.setdefault(charecter, 0)
   count[charecter] = count[charecter] + 1 
   
pprint.pprint(count)