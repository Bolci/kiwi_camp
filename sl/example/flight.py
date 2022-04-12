class Flight():
    def __init__(self, record):    
        self.record = record
        self.target_city = None
    
    def add_target_city(self, target_city):
        self.target_city = target_city
