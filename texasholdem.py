#for every card c in Hand H, x = c % 13
#royal_flush = [12, 11, 10, 9, 8] and same_suit
#straight_flush = straight and same_suit
#four_of_kind = [x, x, x, x, y]
#full_house = three_of_kind and pair
#flush = same_suit
#straight = [x, x+1, x+2, x+3, x+4]
#three_of_kind = [x, x, x, y, z]
#pair = [x, x, y, z, a]
#same_suit = (c / 13) == y
#high_card = max(H)

#Keeping the above for now but we can probably remove soon

hands = {'royal_flush' : [[51, 50, 49, 48, 47], [39, 38, 37, 36, 35, 34], [25, 24, 23, 22, 21], [12, 11, 10, 9, 8]], \
        'straight_flush' : [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9], \
            [6, 7, 8, 9, 10], [7, 8, 9, 10, 11], [8, 9, 10, 11, 12], [13, 14, 15, 16, 17], [14, 15, 16, 17, 18], [15, 16, 17, 18, 19], \
            [16, 17, 18, 19, 20], [17, 18, 19, 20, 21], [18, 19, 20, 21, 22], [19, 20, 21, 22, 23], [20, 21, 22, 23, 24], [21, 22, 23, 24, 25], \
            [26, 27, 28, 29, 30], [27, 28, 29, 30, 31], [28, 29, 30, 31, 32], [29, 30, 31, 32, 33], [30, 31, 32, 33, 34], [31, 32, 33, 34, 35], \
            [32, 33, 34, 35, 36], [33, 34, 35, 36, 37], [34, 35, 36, 37, 38], [39, 40, 41, 42, 43], [40, 41, 42, 43, 44], [41, 42, 43, 44, 45], \
            [42, 43, 44, 45, 46], [43, 44, 45, 46, 47], [44, 45, 46, 47, 48], [45, 46, 47, 48, 49], [46, 47, 48, 49, 50], [47, 48, 49, 50, 51]], \
        'flush' : [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9], \
            [6, 7, 8, 9, 10], [7, 8, 9, 10, 11], [8, 9, 10, 11, 12]]}
#MUST DO (X % 13) BEFORE USING FLUSH IN DICTIONARY


class Card(object):
    def __init__(self, number, in_hand):
        self.number = number #number of card 0-51 (int)
        #suit determined by floor(number / 10)
        #Club,Diamond,Heart,Spade
        self.in_hand = in_hand #bool


class PotentialHand(object):
    def __init__(self, complete, likely, sum, have, need):
        self.complete = complete
        self.likely = likely
        self.sum = sum
        self.have = have
        self.need = need


class Hand(object):
    def __init__(self, cards, potential_hands, prob):
        self.cards = cards #array of cards (int[])
        self.potential_hands = potential_hands
        self.prob = prob #probability matrix/array
    def generatePotential(self):
        matchingSuitHands = []
        matchingNumberHands = []
        moduloCards = []
        for card in self.cards:
            #keep track of initial card suit
            sameSuitTest = card / 13
            #holders for checking matching suit and number
            matchingSuitHand = []
            matchingNumbers = []
            #disregard suit for checking flush
            moduloCards.append(card % 13)
            for card2 in self.cards:
                if (card2 / 13) == sameSuitTest:
                    matchingSuitHand.append(card2)
                if (card2 % 13) == (card % 13):
                    matchingNumbers.append(card2)
            if len(matchingSuitHand) >= 5:
                matchingSuitHands.append(matchingSuitHand)
            if len(matchingNumbers) > 1:
                matchingNumberHands.append(matchingNumbers)

        #NEED TO DETERMINE LIKELY AND SUM
        #NEED PROGRESS FOR FULL HOUSE
        #^^^ I think I'll check the PotentialHands for pairs and 3 of a kind to avoid gross code

        #check for royal flush
        if self.cards in potential_hands['royal_flush']: #if cards match list from dict key, search for index of matching list and get list[index]
            potential_hands.append(PotentialHand(1, 1, 1, potential_hands['royal_flush'][potential_hands['royal_flush'].index(self.cards)], []))

        #check for straight flush
        if self.cards in potential_hands['straight_flush']:
            potential_hands.append(PotentialHand(1, 1, 1, potential_hands['straight_flush'][potential_hands['royal_flush'].index(self.cards)], []))

        #check for flush
        if moduloCards in potential_hands['flush']:
            potential_hands.append(PotentialHand(1, 1, 1, potential_hands['flush'][potential_hands['flush'].index(self.cards)], []))

        #check for matching number
        for numlist in matchingNumberHands:
            #find need by checking which cards of the number are not in the current list
            need = []
            cardnum = numlist[0] % 13
            for num in [cardnum, cardnum + 13, cardnum + 26, cardnum + 39]:
                if num not in numlist:
                    need.append(num)
            if len(numlist) == 4:
                potential_hands.append(PotentialHand(100, 1, 1, numlist, [])) #4 of a kind
            if len(numlist) == 3:
                potential_hands.append(PotentialHand(100, 1, 1, numlist, [])) #3 of a kind
                potential_hands.append(PotentialHand(75, 1, 1, numlist, need)) #partial 4 of a kind
            if len(numlist) == 2:
                potential_hands.append(PotentialHand(100, 1, 1, numlist, [])) #pair
                potential_hands.append(PotentialHand(75, 1, 1, numlist, need)) #partial 3 of a kind
                potential_hands.append(PotentialHand(50, 1, 1, numlist, need)) #partial 4 of a kind

        #check for matching suit
        for numlist in matchingSuitHands:
            #find need by checking which cards of the suit are not in the current list
            cardsuit = numlist[0] / 13
            for num in range(0+13(cardsuit),(12+13(cardsuit))+1):
                if num not in numlist:
                    need.append(num)
            if len(numlist) == 4:
                potential_hands.append(PotentialHand(80, 1, 1, numlist, need)) #4 of matching suit
            if len(numlist) == 3:
                potential_hands.append(PotentialHand(60, 1, 1, numlist, need)) #3 of matching suit
            if len(numlist) == 2:
                potential_hands.append(PotentialHand(40, 1, 1, numlist, need)) #2 of matching suit


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

    def __init__(self, chips, table, hand, potential_hand, ActionObject):
        self.chips = chips
        self.table = table
        self.hand = hand
        self.round_number = ActionObject.round_number
        self.potential_hands = potential_hand
        self.has_completed = False
        self.has_partial_complete = False
        self.action = self.act(ActionObject)

        for potential in self.potential_hands:
            if potential.completed == 1:
                self.has_completed = True
            if potential.completed > .75:
                self.has_partial_complete = True

    def act(self, ActionObject):
        if ActionObject.action == "Check":  # We can add a condition later that bets if we have a hand of a given score
            return self.check_procedure()

        if ActionObject.action == "Bet":
            return self.raise_procedure(ActionObject.raise_size)

    def check_procedure(self):
        # if self.round_number >= 3:
        return "Check"

    def raise_procedure(self, raise_size):
        # Betting procedure for the first round, if we have completed stay in else fold
        if self.round_number < 1:
            if self.has_completed:
                return "Raise", raise_size
            else:
                return "Fold"

        if self.has_completed or self.has_partial_complete:
            return "Raise", raise_size


# A dummy class used to simulate the data structure given to us by the simulation
class ActionObject(object):

    def __init__(self, round_number, action_needed, max_bet_size, cards_on_table):
        self.round_number = round_number
        self.action = action_needed
        self.max_bet_size = max_bet_size
        self.cards_on_table = cards_on_table




p = WeightMatrix()
p.display()
