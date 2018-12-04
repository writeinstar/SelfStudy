__author__ = 'devlmj'
class Animal:

    def eat(self):
        print("eat")

    def drink(self):

        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("run")


class Dog(Animal):

    def bark(self):

        print("bark")


class XiaoTianQuan(Dog):

    def fly(self):

        print("I can fly")

    def bark(self): # extend method

        print("I can bark like a man")
        super().bark()
        # Dog.bark(self)   suport 2.x 3.x but not recommend
        print("##¤%%&&")

class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("private method %d %d" % (self.num1, self.__num2))

    def test(self):
        print("father class public attribute %" % self.num1)
        self.__test()

class B(A):

    def demo(self):

        print(" child class call father public attribute %d" % self.num1)

# sub class can not call father class private attribute and method
        # print("Try to call father class private attribute %d" %self.__num2)
        # self.__test()
# can call this way ,not recommended
        # print("Try to call father class private attribute %d" %self._A__num2) # _A__num2
        # self._A__test()
#如果父类的公有方法访问了父类私有属性，方法
#那么子类可以通过父类公有方法间接访问父类私有属性，方法
b = B()
b.demo()

print(dir(b))
Wangcai = XiaoTianQuan()
Wangcai.eat()
Wangcai.bark()