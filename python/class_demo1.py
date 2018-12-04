__author__ = 'devlmj'

class Cat:

    def eat(self):
        print("cat likes eating fish")
        print("%s likes eating fish" %self.name)# 哪个对象调用的方法，self就是哪个对象的引用

    def drink(self):
        print("Cat drink water")

tom = Cat()
tom.name = "Tom" # 给对象增加属性，不推荐使用
tom.eat()
tom.drink()

print(tom)
print("%d"% id(tom))

lazy_cat = Cat()
lazy_cat.name = "lazy cat"
lazy_cat.drink()
lazy_cat.eat()
print(lazy_cat )
