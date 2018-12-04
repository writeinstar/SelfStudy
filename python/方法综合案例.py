__author__ = 'devlmj'
class Game(object):

    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("help info:")

    @classmethod
    def show_top_score(cls):
        print("Top score : %d" % cls.top_score)

    def start_game(self):
        print("%s is playing game" % self.player_name)

Game.show_help()
Game.show_top_score()
game = Game("player1")

game.start_game()
