import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        x = self.cords[0] + dx * self.speed
        y = self.cords[1] + dy * self.speed
        z = self.cords[2] + dz * self.speed
        if z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self.cords = [x, y, z]

    def get_cords(self):
        print(f'X: {self.cords[0]}, Y: {self.cords[1]}, Z: {self.cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        random_int = random.randint(1, 4)
        print(f'Here are(is) {random_int} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        z = self.cords[2] - abs(dz) * .5 * self.speed
        self.cords[2] = max(z, 0)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = 'Click-click-click'

    def __init__(self, speed):
        super().__init__(speed)

    def speak(self):
        print(self.sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()