class Enemy:
    """ You cant actually overload functions and methods in Python, but you can get the same effect
    of calling different overloaded methods by using named parameters with default values (i.e. name, enemy,
    hit_points below). Refer to main.py on how to create Trolls by passing different arguments"""
    def __init__(self, name="Enemy", hit_points=0, lives=1):  # optional named parameters in __init__ method
        self.name = name
        self.hit_points = hit_points
        self.__hit_points_per_life = hit_points
        self.lives = lives

    @property
    def hit_points(self):
        return self._hit_points

    @hit_points.setter
    def hit_points(self, hit_points):
        if hit_points < 0:
            # print(f'Enemy.hit_points(self, hit_points): Attempting to set hit_points to {hit_points}. Hit point can only be greater than or equal to zero')
            raise AssertionError
        self._hit_points = hit_points

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, lives):
        if lives < 0:
            # print(f'Enemy.lives(self, lives): Attempting to set lives to {lives}. Lives cannot be negative')
            raise AssertionError
        self._lives = lives

    def _get_lives_lost(self, damage):
        """
        Given damage, this method returns the number of lives lost. Each life holds
        __hit_points_per_life. Each time a damage is taken a number of live(s)
        containing hit-points are taken away as much as damage can eat lives
        :param damage (int) : Can be any non-negative number
        :return (int): lives_lost
        """
        lives_lost = 0
        if damage >= self.__hit_points_per_life:
            lives_lost = damage//self.__hit_points_per_life
        else:  # damage < self.__hit_points_per_life
            if self.hit_points - damage >= 0:
                lives_lost = 0    # damage does not break the next lives ceiling
            else:
                lives_lost = 1    # damage breaks the next lives ceiling
        return lives_lost

    def _get_total_hit_points(self):
        return ((self.lives-1) * self.__hit_points_per_life) + self.hit_points

    def _get_hit_points_remaining(self, lives_lost, damage):
        remaining_hit_points = 0
        if self.lives - lives_lost > 0:  # there will be some live(s) left
            # calculate total remaining hit points after lives_lost
            remaining_hit_points = self._get_total_hit_points() - damage
            # calculate remaining hit points considering the lives to be left
            while remaining_hit_points >= self.__hit_points_per_life:
                remaining_hit_points -= self.__hit_points_per_life
        return remaining_hit_points

    def take_damage(self, damage):
        lives_lost = self._get_lives_lost(damage)
        hit_points_remaining = self._get_hit_points_remaining(lives_lost, damage)
        if self.lives - lives_lost >= 0:
            self.lives -= lives_lost
        else:
            self.lives = 0  # damage is too big, it killed the enemy immediately
        self.hit_points = hit_points_remaining

    def __str__(self):
        return f'Name: {self.name}, Lives: {self.lives}, hit points: {self.hit_points}'

    def __eq__(self, other):
        return self.name == other.name and self.__hit_points_per_life == other.hit_points_per_live and self.hit_points == other.hit_points and set.lives == other.lives

    def __ne__(self, other):
        return not self.__eq__(other)


class Troll(Enemy):
    def __init__(self, name):
        # Enemy.__init__(self, name=name, hit_points=23, lives=1)
        super(Troll, self).__init__(name=name, hit_points=23, lives=1)

    def grunt(self):
        print("Me {0.name}. {0.name} stop you".format(self))


class Vampyre(Enemy):
    def __init__(self, name):
        super().__init__(name, hit_points=12, lives=3)

