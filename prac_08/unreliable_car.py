from car import Car
import random
class UnreliableCar(Car):
    distance = 0

    def __init__(self, name, fuel, reliability):
        super().__init__()
        self.reliability = reliability

    def drive(self, distance):
        super().drive(distance)
        distance_1 = float(random.randint(0, 100))
        distance += distance_1
        if distance < self.reliability:
            return distance
        else:
            return print('Unreliable')


