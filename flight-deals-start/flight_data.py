class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, fly_from_state, fly_to_state, fly_from_airport, fly_to_airport, flight_date, return_date):
        self.price = price
        self.fly_from_state = fly_from_state
        self. fly_to_state = fly_to_state
        self.fly_from_airport = fly_from_airport
        self.fly_to_airport = fly_to_airport
        self.flight_date = flight_date
        self.return_date = return_date
