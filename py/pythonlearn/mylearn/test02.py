#coding=utf-8

a = [1,2,3,4]
print a

a.reverse()
print a

tuple1 = (1,2,[11,22])
print tuple1

tuple1[2][1] = 33
print tuple1

dict = {"name":"zhangsan","age":18}
for item in dict.items():
	print item
	item[1] = 1212
	print item

print dict