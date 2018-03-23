#coding=utf-8

num1 = 11
num2 = 11.6
res = num1 + num2

print res
print type(num1)
print type(num2)
print type(res)

#password = raw_input("请输入密码:")
#print '您刚刚输入的密码是:'  ,password

#反转字符串
str = 'abcdef'
print str
print str[::-1]

mystr = 'hello world itcast and itcastcpp'
res = mystr.find('itcast', 13, len(mystr))
print res

res = mystr.split(' ',2)
print res

res = mystr.partition("itcast")
print res
