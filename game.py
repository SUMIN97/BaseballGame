class Game:
    def __init__(self):
        self.answer = "123"
    def guess(self, guessNumber):
        self.assert_illegal_value(guessNumber)

        strike = 0
        balls = 0
        solved = 'false'

        for i in range(len(self.answer)):
            if guessNumber[i] == self.answer[i]:
                strike +=1
            elif guessNumber[i] in self.answer:
                balls +=1

        if strike == len(self.answer):
            solved = 'true'
        res = f'solved = {solved}, strikes = {strike}, balls = {balls}'

        return res

    def assert_illegal_value(self, guessNumber):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:
            raise TypeError()
        for number in guessNumber:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()
        if self.isDuplicatedNumber(guessNumber):
            raise TypeError()

    def isDuplicatedNumber(self, guessNumber):
        return guessNumber[0] == guessNumber[1] or \
            guessNumber[0] == guessNumber[2] or \
            guessNumber[1] == guessNumber[2]

