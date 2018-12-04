__author__ = 'devlmj'


class MusicPlayer(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):

        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):# 初始化动作只执行一次
         if MusicPlayer.init_flag:
             return
         print("Initialize")
         MusicPlayer.init_flag = True



player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)