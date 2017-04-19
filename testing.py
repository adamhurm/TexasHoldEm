import unittest
from texasholdem import *


class UnitTesting(unittest.TestCase):

    def test_naive(self):
        self.assertEqual(1, 1)

    def test_check_procedure(self):
        action_obj = ActionObject(1, "Check", 100, [])
        table = Table([], 100)
        game = Game(100, table, [1, 2], [[]], action_obj)

        self.assertEqual(game.action(), "Check")





if __name__ == '__main__':
    unittest.main()