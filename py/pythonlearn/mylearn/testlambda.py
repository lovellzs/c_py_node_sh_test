#coding=utf-8

stus = [
    {"name":"zhangsan", "age":18}, 
    {"name":"lisi", "age":19}, 
    {"name":"wangwu", "age":17}
]

stus.sort(key = lambda x:x['name'])

print stus