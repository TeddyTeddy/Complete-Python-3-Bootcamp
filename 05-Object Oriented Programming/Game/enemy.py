class Enemy:
    """ You cant actually overload functions and methods in Python, but you can get the same effect
    of calling different overloaded methods by using named parameters with default values (i.e. name, enemy,
    hit_points below). Refer to main.py on how to create Trolls by passing different arguments"""
    def __init__(self, name="Enemy", hit_points=0, lives=1):  # optional named parameters in __init__ method
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print(f'I took {damage} points and have left {self.hit_points} left')
        else:
            self.lives -= 1

    def __str__(self):
        return f'Name: {self.name}, Lives: {self.lives}, hit points: {self.hit_points}'


class Troll(Enemy):
    def __init__(self, name):
        # Enemy.__init__(self, name=name, hit_points=23, lives=1)
        super(Troll, self).__init__(name=name, hit_points=23, lives=1)

