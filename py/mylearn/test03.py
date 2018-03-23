#coding=utf-8

def test(a,b):
	'''用来完成对2个数求和'''
	print("%d"%(a+b))
test(11,22)

#help(test)

def resInfo():
	return 11 , 33

age1,age2 = resInfo()
print age1,age2
print resInfo()

def selfAdd(a):
	'''  自增 '''
	a = a+a

a_int = 1
selfAdd(a_int)
print a_int

a_list = [1,2]
selfAdd(a_list)
print a_list
