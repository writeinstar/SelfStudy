__author__ = 'devlmj'

class Dog(object):

    @staticmethod
    def run():
        print("Dog is running")

Dog.run() # 不需要创建类对象，直接调用类方法