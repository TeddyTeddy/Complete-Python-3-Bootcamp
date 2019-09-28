class Player:
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print(f'Player.__set_lives(self, lives): lives argument cannot be negative: {lives}')
            self._lives = 0

    def _get_lives(self):
        return self._lives

    def _set_level(self, level):
        if level < 1:
            self._score -= (self._level - 1) * 1000
            self._level = 1
        else:  # level >= 1
            self._score += (level - self._level) * 1000  # then bump up/down the score accordingly
            self._level = level

    def _get_level(self):
        return self._level

    level = property(_get_level, _set_level)
    lives = property(_get_lives, _set_lives)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return f'Player: name is {self.name} - lives is {self._lives} - level is {self.level} - score {self._score}'
