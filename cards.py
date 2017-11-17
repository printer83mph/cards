import random

class Card(object):

    def __init__(self, up = False):
        self.up = up

class NumberedCard(Card):

    def __init__(self, up = False, number = 0):
        self.number = number
        self.up = up

    def get_name(self):
    	return str(self.number)

class FrenchCard(NumberedCard):

    def __init__(self, up = False, number = 0, suit = "spades"):
        self.number = number
        self.suit = suit
        self.up = up
        self.specials = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

    def get_name(self):
        return str(self.number if self.number not in self.specials else self.specials[self.number]) + " of " + self.suit

class Pile(object):

    def __init__(self, cards = None):
        if(cards != None):
            cards = []
        self.cards = cards

    def fill(self, replace = True):
        self.cards = [] if replace else self.cards
        for i in range(1,10):
            self.cards.append(NumberedCard(False,i))

    def get_top_card(self):
        return self.cards[-1]

    def shuffle(self):
        random.shuffle(self.cards)

    def french_fill(self, replace = True):
        self.cards = [] if replace else self.cards
        suits = ["spades","hearts","clubs","diamonds"]
        for i in range(0,4):
            for s in range(1,14):
                self.cards.append(FrenchCard(False,s,suits[i]))

    def get_names(self):
        return [card.get_name() for card in self.cards]

    def print_pile(self):
   		for card in self.cards:
   			print card.get_name()

    def pull_card(self, index):
    	card = self.cards[index]
    	del self.cards[1]
    	return card

    def pull_random_card(self):
        return self.pull_card(random.randint(0,len(self.cards)))

    def random_card(self):
        return random.choice(self.cards)

def main():
    cards = Pile()
    cards.french_fill()
    cards.print_pile()
    x = cards.pull_random_card()
    cards.print_pile()
    print x.get_name()

if __name__ == "__main__":
    main()