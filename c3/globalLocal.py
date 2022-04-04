def spam():
	global eggs
	print(hams)		#this is the gloabl
	bbqs = 'local'	#this is the local
	eggs = 'spam'

eggs = 'global'
hams = 'global'
bbqs = 'global'
spam()
print(eggs)
print(hams)
print(bbqs)