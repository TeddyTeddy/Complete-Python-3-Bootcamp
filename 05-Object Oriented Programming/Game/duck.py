class Duck(object):
    def walk(self):
        print('Waddle, waddle, waddle')

    def swim(self):
        print('Come on in, the water is lovely')

    def quack(self):
        print('Quack Quack')

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
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)  # a Penguin is passing the duck test. No error
