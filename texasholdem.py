from deuces import Evaluator
from deuces import Card
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

classes_need = {'royal_flush' : 5, 'straight_flush' : 5, "four_kind" : 4, 'full_house' : 5, \
                'flush' : 5, 'straight' : 5, 'three_kind' : 3, 'two_pair': 4, 'pair': 2} #number of cards needed for a class
deucify = {} #might need to be function, create deuces Card out of int
#MUST DO (X % 13) BEFORE USING FLUSH IN DICTIONARY


class Card(object):
    def __init__(self, number, in_hand):
        self.number = number #number of card 0-51 (int)
        #suit determined by floor(number / 13)
        #Club,Diamond,Heart,Spade
        self.in_hand = in_hand #bool


class PotentialHand(object):
    def __init__(self, complete, likely, sum, have, rank):
        self.complete = complete
        self.likely = likely
        self.sum = sum
        self.have = have
        self.rank = rank


class Hand(object):
    def __init__(self, cards, table, potential_hands):
        self.cards = cards #array of cards (int[])
        self.board = table.cards
        self.potential_hands = potential_hands
    def generatePotential(self):
        matching_suit_hands = []
        matching_number_hands = []
        moduloCards = []
        cards = [] #will replace self.cards for poker.py
        cards.append(self.cards)
        cards.append(self.board)

        for card in cards:
            #keep track of initial card suit
            sameSuitTest = card / 13
            #holders for checking matching suit and number
            matching_suit_hand = []
            matching_numbers = []
            #disregard suit for checking flush
            moduloCards.append(card % 13)
            for card2 in cards:
                if (card2 / 13) == sameSuitTest:
                    matching_suit_hand.append(card2)
                if (card2 % 13) == (card % 13):
                    matching_numbers.append(card2)
            if len(matching_suit_hand) >= 5:
                matching_suit_hands.append(matching_suit_hand)
            if len(matching_numbers) > 1:
                matching_number_hands.append(matching_numbers)

        #NEED TO DETERMINE LIKELY AND SUM

        score = evaluator.evaluate(self.cards, self.table)

        #check for royal flush
        if self.cards in hands['royal_flush']: #if cards match list from dict key, search for index of matching list and get list[index]
            keep = hands['royal_flush'][hands['royal_flush'].index(self.cards)]
            self.potential_hands.append(PotentialHand(100, 1, score, keep, []))

        #check for straight flush
        if self.cards in hands['straight_flush']:
            keep = hands['straight_flush'][hands['royal_flush'].index(self.cards)]
            self.potential_hands.append(PotentialHand(100, 1, score, keep, []))

        #check for flush
        if moduloCards in hands['flush']:
            keep = hands['flush'][hands['flush'].index(self.cards)]
            self.potential_hands.append(PotentialHand(100, 1, score, keep, []))

        #check for matching number
        for numlist in matching_number_hands:
            #find need by checking which cards of the number are not in the current list
            need = []
            cardnum = numlist[0] % 13
            for num in [cardnum, cardnum + 13, cardnum + 26, cardnum + 39]:
                if num not in numlist:
                    need.append(num)
            if len(numlist) == 4:
                potential_hands.append(PotentialHand(100, 1, score, numlist, [])) #4 of a kind
            if len(numlist) == 3:
                potential_hands.append(PotentialHand(100, 1, score, numlist, [])) #3 of a kind
                potential_hands.append(PotentialHand(75, 1, score, numlist, need)) #partial 4 of a kind
            if len(numlist) == 2:
                potential_hands.append(PotentialHand(100, 1, score, numlist, [])) #pair
                potential_hands.append(PotentialHand(75, 1, score, numlist, need)) #partial 3 of a kind
                potential_hands.append(PotentialHand(50, 1, score, numlist, need)) #partial 4 of a kind

        #check for matching suit
        for numlist in matching_suit_hands:
            #find need by checking which cards of the suit are not in the current list
            cardsuit = numlist[0] / 13
            for num in range(0+13(cardsuit),(12+13(cardsuit))+1):
                if num not in numlist:
                    need.append(num)
            if len(numlist) == 4:
                potential_hands.append(PotentialHand(80, 1, score, numlist, need)) #4 of matching suit
            if len(numlist) == 3:
                potential_hands.append(PotentialHand(60, 1, score, numlist, need)) #3 of matching suit
            if len(numlist) == 2:
                potential_hands.append(PotentialHand(40, 1, score, numlist, need)) #2 of matching suit
        
        pairs = []
        threes = []
        #gather complete pairs and 3ok's
        for hand in potential_hands:
            if hand.complete == 100:
                if len(hand.have) == 3:
                    threes.append(hand)
                if len(hand.have == 2):
                    pairs.append(hand)
        #grab best pair and 3ok
        if pairs or threes:
            #if more than 
            maxpair = []
            for pair in pairs:
                if (pair[0] % 13) > (maxpair[0] % 13):
                    maxpair = pair
            maxthree = []
            for three in threes:
                if (three[0] % 13) > (maxthree[0] % 13):
                    maxthree = three
            if pairs and threes:
                potential_hands.append(PotentialHand(100, 1, score, maxpair.extend(maxthree)))
            if threes:
                potential_hands.append(PotentialHand(100, 1, score, maxthree)
            if len(pairs) >= 2:
                potential_hands.append(PotentialHand(100, 1, score, pairs[0].extend(pairs[1])))
            if len(pairs) == 1:
                potential_hands.append(PotentialHand(100, 1, score, maxpair))
                potential_hands.append(PotentialHand(50, 1, score, maxpair))
            


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


class Game(object):

    def __init__(self, chips, table, hand, ActionObject):
        self.chips = chips
        self.table = table
        self.hand = hand
        self.round_number = ActionObject.round_number
        self.potential_hands = self.hand.potential_hands
        self.has_completed = False
        self.has_partial_complete = False
        # self.action = self.act(ActionObject)

        for potential in self.potential_hands:
            if potential.complete == 1:
                self.has_completed = True
            if potential.complete > .75:
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
        if self.round_number <= 1:
            if self.has_completed:
                return "Raise", raise_size
            else:
                return "Fold"

        if self.has_completed or self.has_partial_complete:
            return "Raise", raise_size


# A dummy class used to simulate the data structure given to us by the simulation
class ActionObject(object):

    def __init__(self, round_number, action_needed, max_bet_size, raise_size, cards_on_table):
        self.round_number = round_number
        self.action = action_needed
        self.max_bet_size = max_bet_size
        self.raise_size = raise_size
        self.cards_on_table = cards_on_table