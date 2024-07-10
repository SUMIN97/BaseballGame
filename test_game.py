from unittest import TestCase
from game import Game
class TestGame(TestCase):

    def setUp(self):
        super().setUp()
        self.game = Game()

    def assert_illegal_argument(self, guessNumber):
        try:
            self.game.guess(guessNumber)
            self.fail()
        except TypeError:
            print('hi')
            pass
    def test_exception_when_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("12s")
        self.assert_illegal_argument("121")

    def test_return_solve_result_if_matched_number(self):
        self.game.answer = "123"

        res = self.game.guess(self.game.answer)
        self.assertEqual("solved = true, strikes = 3, balls = 0",
                         res)

        res = self.game.guess("456")
        self.assertEqual("solved = false, strikes = 0, balls = 0",
                         res)

        res = self.game.guess("129")
        self.assertEqual("solved = false, strikes = 2, balls = 0",
                         res)

        res = self.game.guess("240")
        self.assertEqual("solved = false, strikes = 0, balls = 1",
                         res)

        res = self.game.guess("321")
        self.assertEqual("solved = false, strikes = 1, balls = 2",
                         res)







