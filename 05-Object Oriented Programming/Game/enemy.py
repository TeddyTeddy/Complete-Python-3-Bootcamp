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

    def _get_total_hit_points(self):
        return ((self.lives-1) * self.__hit_points_per_life) + self.hit_points

    def take_damage(self, damage):
        total_hit_points = self._get_total_hit_points()
        remaining_hit_points = total_hit_points - damage
        if remaining_hit_points <= 0:
            # damage was too big to kill the instance
            self.lives = 0
            self.hit_points = 0
        else: # there are remaining hit points, calculate lives and hit_points
            if remaining_hit_points % self.__hit_points_per_life == 0:
                # remaining_hit_points are a multiple of hit_points_per_life
                self.lives = remaining_hit_points // self.__hit_points_per_life
                self.hit_points = self.__hit_points_per_life
            else:
                self.lives = (remaining_hit_points // self.__hit_points_per_life) + 1
                self.hit_points = remaining_hit_points % self.__hit_points_per_life

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

