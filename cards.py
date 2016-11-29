class Card(object):

    def __init__(self,up = False):
        self.up = up

class NumberedCard(Card):

    def __init__(self,number = 0,up = False):
        self.number = number
        self.up = up

class FrenchCard(NumberedCard):

    def __init__(self,number = 0,suit = "spades",up = False):
        self.number = number
        self.suit = suit
        self.up = up

class Pile(object):

    def __init__(self,cards = None):
        if(cards != None):
            cards = []
        self.cards = cards
