__author__ = 'devlmj'
class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

        print("assign address")
        return super().__new__(cls)

    def __init__(self):
        print("Player initialize")


player = MusicPlayer()

print(player)