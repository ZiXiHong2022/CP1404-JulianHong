from taxi import Taxi
taxi_detail = Taxi("Prius 1", 100)
taxi_detail.current_fare_distance = 40
print(taxi_detail)
print(taxi_detail.get_fare())


taxi_detail.start_fare()
taxi_detail.current_fare_distance = 100
print(taxi_detail)
print(taxi_detail.get_fare())

