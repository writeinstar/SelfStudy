__author__ = 'devlmj'
class Cat:
    def __init__(self, new_name):

        self.name = new_name
        print("%s initialization" % new_name)
    def __del__(self):
        print("%s delete" % self.name)
# tom is global variable
tom = Cat("tom")
print(tom.name)
# del tom
print("-" * 50)