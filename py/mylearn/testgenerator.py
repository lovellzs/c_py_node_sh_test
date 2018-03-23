#coding=utf-8

def fib(times):
	n = 0
	a,b = 0,1
	while n<times:
		yield b
		a , b = b ,a+b
		n +=1
	# return 'done'


F = fib(5)

print	next(F)
print	next(F)
print	next(F)
print	next(F)
print	next(F)

for n in fib(5):
	print n


def gen():
	i = 0
	while i<5:
		temp = yield i
		print "asas",(temp)

		i+=1
	# return 'done'

for n in gen():
	print n