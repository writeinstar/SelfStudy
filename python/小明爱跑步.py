__author__ = 'devlmj'
class Person:
    def __init__(self, pname ,pweight):
        self.name = pname # self.attribute =
        self.weight = pweight

    def __str__(self):
        return "My name is %s ,weight is %.2f kg"%(self.name, self.weight)

    def run(self):
        print("%s run" % self.name )
        self.weight -= 0.5

    def eat(self):
        print("%s eat again" % self.name)
        self.weight += 1

xiaoming = Person("xiaoming", 75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)