class Card(object):

    def __init__(self,up = False):
        self.up = up

class NumberedCard(Card):

    def __init__(self,number = 0):
        self.number = number

class FrenchCard(NumberedCard):

    def __init__(self,number = 0,suit = "spades"):
        self.number = number
        self.suit = suit
