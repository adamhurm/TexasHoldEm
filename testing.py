import unittest
from texasholdem import *


class UnitTesting(unittest.TestCase):

    def test_naive(self):
        self.assertEqual(1, 1)

    def test_check_procedure(self):
        action_obj = ActionObject(1, "Check", 100, 20, [])
        table = Table([], 100)
        hand = Hand([1,2], [], .1)
        game = Game(100, table, hand, action_obj)
        self.assertEqual(game.act(action_obj), "Check")

    def test_raise_procedure(self):
        action_obj = ActionObject(1, "Bet", 100, 20, [])
        table = Table([], 100)
        hand = Hand([1, 2], [], .1)
        game = Game(100, table, hand, action_obj)
        self.assertEqual(game.round_number, 1)
        self.assertFalse(game.has_completed)
        self.assertEqual(game.act(action_obj), "Fold")
        print("Passed Folding case")

        potential_hand_test = PotentialHand(1, 0, 600, [2, 3, 4, 5], [])
        hand2 = Hand([1, 2], [potential_hand_test], .1)
        game = Game(100, table, hand2, action_obj)
        self.assertEqual(game.act(action_obj), "Raise")









if __name__ == '__main__':
    unittest.main()