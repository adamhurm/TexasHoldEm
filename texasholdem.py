class Card(object):
    def __init__(self, number, inHand):
        self.number = number #number of card 0-51 (int)

        # suit determined by floor(number / 10)
        # Club(1),Diamond(2),Heart(3),Spade(4)
        if number / 13 <= 4:
            self.suit = 4  # Spade
        if number / 13 <= 3:
            self.suit = 3  # Heart
        if number / 13 <= 2:
            self.suit = 2  # Diamonds
        if number / 13 <= 1:
            self.suit = 1  # Clubs

        self.inHand = inHand #bool
        # self.mod_number = number %

    def __str__(self):
        return self.number, self.suit


class Hand(object):
    def __init__(self, cards):
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


class WeightMatrix(object):

    def __init__(self):
       # self.cards = cards #array of cards (int[])
        self.cards = []
        self.cards_already_examined = []
        self.current_hand_value = 0
        self.cards.append(20) # This accounts for 0 being Two

        for i in range(1, 52):  # This just populates the matrix with
            mod_val = i % 13
            if mod_val == 0:  # This if statement is necessary because 0 = Two and 12 = Ace
                if i == 13 or i == 26 or i == 39 or i == 52:
                    self.cards.append(20)
            else:
                self.cards.append(mod_val * 10 + 20)  # Add 20 to account for 0 == Two

    def update(self, cards):
        return

    def display(self):
        print(self.cards)



class Game(object):

    def __init__(self):
        self.chips = Chips




p = WeightMatrix()
p.display()
