class User:
    def __init__ (self, firstname, lastname, email, score):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.score = score

    def full_name(self):
        print(f'{self.firstname} {self.lastname}')

class VipUser(User):
    def __init__(self):
        super().__init__()

    def full_name(self):
        old_text = super().full_name()
        return '*' + old_text + '*'

VIP = VipUser()

VIP.full_name()

class Vehicle:
    def __init__(self, name):
        self.name = name
        self.wheels_quantity = 1
        print('Initializing', self.name)

    def drive(self):
        print('Driving')

    def stop(self):
        print('Stopped')


class Unicycle(Vehicle):
    def balance(self):
        print('Trying not to fall down')


class Bicycle(Vehicle):
    def __init__(self, name):
        super().__init__(name)  # Vehicle.__init__(self, name)
        self.wheels_quantity = 2

    def ring(self):
        print('Ringing!')

    def drive(self):
        super().drive()  # Vehicle.drive(self)
        print('All i want is bicycle!')


class MountainBicycle(Bicycle):
    def drive(self):
        super().drive()
        print('Sometimes hiking always biking')


if __name__ == '__main__':
    something = Vehicle('Unknown')
    canondale = Bicycle('Canondale')
    unicycle = Unicycle('Unicykl')
    mtb = MountainBicycle('Specialized')
    print(mtb.name)
    print(mtb.wheels_quantity)
    mtb.drive()
    mtb.stop()
    mtb.ring()