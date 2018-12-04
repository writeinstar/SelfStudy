
__author__ = 'devlmj'
class Cat:
    def __init__(self, new_name):

        self.name = new_name
        print("%s initialization" % new_name)
    def __del__(self):
        print("%s delete" % self.name)

    def __str__(self): # 修改此function 打印对象时，打印 自定义内容，而不是类和对象地址
        #must return a string
        return "I am a cat %s" % self.name
# tom is global variable
tom = Cat("tom")
print(tom)
# del tom
