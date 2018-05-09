# coding:utf-8


class Foo(object):
    X = 1.0
    Y = 2.0

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):
        return cls.averag(cls.X, cls.Y)


class Son(Foo):
    X = 1.0
    Y = 2.0

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / 3 + 6

    @classmethod
    def class_method(cls):
        return cls.averag(cls.X, cls.Y) + 11


# 类方法和静态方法都可以被重写
p = Son()
print("====",p.static_method())
print(p.class_method())
# 1.5
# 2.6666666666666665

# 类方法和静态方法都可以被实例调用  都可以用类名称调用
print("====",Son.static_method())
print(Son.class_method())
