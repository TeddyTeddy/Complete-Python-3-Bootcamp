class Wing(object):
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print('I can fly easily')
        elif self.ratio == 1:
            print('This is hard work, but i am flying')
        else:
            print('I think I will just walk')


class Duck(object):
    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print('Waddle, waddle, waddle')

    def swim(self):
        print('Come on in, the water is lovely')

    def quack(self):
        print('Quack Quack')

    def fly(self):
        self._wing.fly()


class Penguin(object):
    def walk(self):
        print('Waddle, waddle, I waddle too')

    def swim(self):
        print('Come on in, the water is ice cold')

    def quack(self):
        print('Penguin quacks')


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)  # a Penguin is passing the duck test. No error
