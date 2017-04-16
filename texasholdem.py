class Card(object):
    def __init__(self, number, inHand):
        self.number = number #number of card 0-51 (int)
        #suit determined by floor(number / 10)
        #Club,Diamond,Heart,Spade
        self.inHand = inHand #bool

class Hand(object):
    def __init__(self, cards, prob):
        self.cards = cards #array of cards (int[])
        self.prob = prob #probability matrix/array

class Table(object):
    def __init__(self, cards, pot):
        self.cards = cards #array of cards (int[])
        self.pot = pot #number of chips (int)

class Chips(object):
    def __init__(self, chips, history):
        self.chips = chips #number of chips (int)
        self.history = history #array of chip count for past moves (int)

    def add(self, chips):
        self.history.append(chips)
        self.chips += chips
    
    def remove(self, chips):
        self.history.append(chips)
        self.chips -= chips

    def getHistory(self, move):
        return self.history[move]

class ProbMatrix(object):
    def __init__(self, cards):
        self.cards = cards #array of cards (int[])

    def update(self):
        return
    def add(self):
        return
    def remove(self):
        return
