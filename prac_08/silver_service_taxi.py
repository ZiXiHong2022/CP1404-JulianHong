from taxi import Taxi

class SilverServiceTaxi(Taxi):
    value = 0

    def __init__(self, name, fuel, fanciness):
        Taxi.__init__(self, name, fuel)
        self.fanciness = fanciness
        self.flag_fall = 4.50

    def fanciness(self, fanciness):
        return float(self.price_per_km) * fanciness

    def total_fare(self):
        fare = self.get_fare()
        return self.flag_fall + fare

    def __str__(self):
        return super().__str__() + "plus flag fall $" + str(self.flag_fall)
















