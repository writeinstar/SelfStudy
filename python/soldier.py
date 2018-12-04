__author__ = 'devlmj'
class Gun:

    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print(" %s bullets are used up" % self.model)
            return

        self.bullet_count -= 1
        print("%s biu ,%d bullets remain" % (self.model, self.bullet_count) )


class Soldier:

    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None: # if self.gun == gun

            print("% hasn't gun" % self.name)
            return
        print("%s fire" % self.name)

        self.gun.add_bullet(50)
        self.gun.shoot()

ak47 = Gun("AK47")

# ak47.add_bullet(50)
# ak47.shoot()

xusanduo = Soldier("xusanduo")
xusanduo.gun = ak47
xusanduo.fire()
print(xusanduo.gun)