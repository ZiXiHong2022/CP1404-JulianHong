from taxi import Taxi

class SilverServiceTaxi(Taxi):
    value = 0

    def __init__(self, name, fuel, price_per_km):
        Taxi.__init__(self, name, fuel)
        self.price_per_km = price_per_km
        self.flag_fall = 4.50

    def fanciness(self, value):
        return float(self.price_per_km) * value

    def total_fare(self):
        fare = self.fanciness(2) * self.current_fare_distance
        return self.flag_fall + fare

    def __str__(self):
        word = super.__str__(self)
        return word + "plus flag fall $" + str(self.flag_fall)
















