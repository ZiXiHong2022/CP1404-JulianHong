from silver_service_taxi import SilverServiceTaxi
def main():
    trip = SilverServiceTaxi("yikes", 100, 2)
    print(trip.total_fare())
    print(trip)
