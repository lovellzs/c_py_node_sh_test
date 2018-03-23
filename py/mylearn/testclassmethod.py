#coding=utf-8

class People(object):
    country = 'china'

    #类方法，用classmethod来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country

p = People()
p.country = "england"
People.country = "japan"
print p.getCountry()    #可以用过实例对象引用
print People.getCountry()    #可以通过类对象引用