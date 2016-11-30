from random import shuffle

class Card(object):

    def __init__(self,up = False):
        self.up = up

class NumberedCard(Card):

    def __init__(self,up = False,number = 0):
        self.number = number
        self.up = up

class FrenchCard(NumberedCard):

    def __init__(self,up = False,number = 0,suit = "spades"):
        self.number = number
        self.suit = suit
        self.up = up

    def get_name(self):

        return str(self.number) + " of " + self.suit

class Pile(object):

    def __init__(self,cards = None):
        if(cards != None):
            cards = []
        self.cards = cards

    def fill(self,replace = True):
        self.cards = [] if replace else self.cards
        for i in range(0,52):
            self.cards.append(NumberedCard(False,i))

    def getTopCard(self):
        return self.cards[-1]

    def shuffle(self):
        random.shuffle(self.cards)

class FrenchPile(Pile):

    def fill(self,replace = True):
        self.cards = [] if replace else self.cards
        suits = ["spades","hearts","clubs","diamonds"]
        for i in range(0,4):
            for s in range(1,14):
                self.cards.append(FrenchCard(False,s,suits[i]))
