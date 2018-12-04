__author__ = 'devlmj'
class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s jump and play" % self.name)

class XiaoTianDog(Dog):

    def game(self):
        print("%s fly and play" % self.name)

class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s and %s play together "% (self.name, dog.name))
        dog.game()

normaldog = Dog("dog1")
flydog = XiaoTianDog("dog2")
xiaomei = Person("Xiaomei")
xiaomei.game_with_dog(normaldog)
xiaomei.game_with_dog(flydog)