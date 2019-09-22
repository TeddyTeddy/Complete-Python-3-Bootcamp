class Car(object):
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod
    def set_wheels(wheels):  # static/class method having no 'self' argument
        Car.wheels = wheels


mustang = Car('Ford', 'Mustang')
carrera = Car('Porshe', 'Carrera')

Car.set_wheels(3)