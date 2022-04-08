class Airport():
    def __init__(self, name):
        self.name = name
        self.flights = []
    
    def add_flight(self, new_flight):
        self.flights.append(new_flight)
    