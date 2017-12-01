from cards import *

class WarGame(object):
    cur_game = None

    def __init__(self, num_cards = 52):
        self.plys = [Pile() for i in range(2)]
        for i in self.plys:
            i.french_fill()
        self.tc = 0

    def move(self):
        (input("Press enter to pull a card, "+i) for i in ("1","2"))
        c0 = self.plys[0].pull_random_card()
        c1 = self.plys[1].pull_random_card()
        winner = 0 if c0.number > c1.number else 1
        if winner == 1:
            if c0.number == c1.number:
                (input("Press enter to pull a card, "+str(i % 2)) for i in range(6))

    def play_game(self,turnlimit = -1):
        while self.tc < turnlimit:
            c1,c1 = ()

def main():
    game = WarGame()

if __name__ == "__main__":
    main()
