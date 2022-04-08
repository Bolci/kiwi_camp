from utils import get_time_interval

class DataExporter():
    def __init__(self,):
        
        #template for data storage
        self.data_format_template = {"flights" : [] , "bags_allowed":0, "bags_count":0, "destination":"", "origin":"", "total_price":0.0, "travel_time":0.0}
    
    @staticmethod
    def parse_connection(flight_list):
        ''' parse flight info from connection objects '''
        return [flight.record for flight in flight_list]
    
    @staticmethod
    def calculate_price(connection,bags_count):
        ''' calculate total price of all requested flights'''
        
        
        
        return sum([
            float(single_flight['base_price'] + bags_count * single_flight['bag_price']) f
            or single_flight in connection
        ])
    
    
    
    @staticmethod
    def calculate_travel_time(flight):
        ''' calculate total travel time '''
        return get_time_interval(flight[-1]['arrival'],flight[0]['departure'])
    
    @staticmethod
    def get_allowed_bags(flights):
        '''parse maximum allowed bags from flight list'''
        return min([flight.record["bags_allowed"] for flight in flights])
    
    def prepare_single_flight(self, flight, bags_requested, destination, origin,bags):
        ''' prepare single flight to desired format'''
        
        
        data_format = self.data_format_template.copy()
        
        data_format["flights"] = self.parse_connection(flight)
        data_format["bags_count"] = bags
        data_format["bags_allowed"] = self.get_allowed_bags(flight)
        data_format["destination"] = destination
        data_format["origin"] = origin
        data_format["total_price"] = self.calculate_price(data_format["flights"],bags)
        data_format["travel_time"] = self.calculate_travel_time(data_format["flights"])
        
        return data_format
    
    @staticmethod
    def sort_by_param(flights,param = "total_price"):
        ''' sort list of flights by parameter'''
        
        return sorted(flights, key=lambda d: d[param]) 
    
    def save_file(self, flights, bags_requested, destination, origin,bags):
        output_file = list(map(lambda flight: self.prepare_single_flight(flight,bags_requested, destination, origin,bags),flights))
        output_file = self.sort_by_param(output_file)
        
       
        print(output_file)
        