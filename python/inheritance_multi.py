__author__ = 'devlmj'

# 如果父类中 有同名方法 属性，避免使用多继承，子类会按__mro__中顺序调用
class A:

    def test(self):
        print(" A test method")

    def demo(self):
        print("A demo")

class B:

    def test(self):
        print(" B test method")

    def demo(self):

        print(" B demo method")

class C (A, B):


    pass

c = C()

print(C.__mro__)
print(dir(C))
print(dir(c))
print(dir(object))
#print(c.__mro__) # why error
c.test()
c.demo()