__author__ = 'devlmj'

class Women:
    def __init__(self, name):
        self.name = name
        self.__age =18

    def __secret(self):
        print("%s is %d years old" % (self.name, self.__age))
    def secret2(self):
        print("%s is %d years old" % (self.name, self.__age))

xiaofang = Women("Fang")

#print(xiaofang.__age)
print(xiaofang._Women__age) # this moethod is not recommended
xiaofang._Women__secret()

xiaofang.secret2()
