from Conection import Conection
from Airport import Airport
from utils import *

class Graph_Database():
    def __init__(self, attributes):
        self.attributes = attributes
        self.airports = []
        
    def add_record(self, single_record):
        ''' add single record to database'''

        record = dict(zip(self.attributes,single_record))
        
        #initial variables
        saved_id_dest = -1
        saved_id_or = -1
        origin_Found = False
        dest_Found = False    
            
        #check if airport exists
        for id_x,single_airport in enumerate(self.airports):
            
            #check for destination airport and save its index if found
            if single_airport.name == record['destination']:
                saved_id_dest = id_x
                dest_Found = True
                
                if origin_Found:
                    break
             
            #check if the city is in the databaae
            if single_airport.name == record['origin']:
                saved_id_or = id_x
                origin_Found = True
                
                if dest_Found:
                    break
                    
        new_conection = Conection(record)
        
        #TODO rewrite
        #process destination
        if not dest_Found:   
            self.airports.append(Airport(record['destination']))
            new_conection.add_target_city(self.airports[-1])
        else:
            new_conection.add_target_city(self.airports[saved_id_dest])                          
        
        #process origin
        if not origin_Found:
            self.airports.append(Airport(record['origin']))
            self.airports[-1].add_connection(new_conection)
            
        else:
            self.airports[saved_id_or].add_connection(new_conection)
            
            
        
    def load_data(self, raw_data):
        ''' load list of lists of data'''
        list(map(self.add_record,raw_data))
    
    def get_id_of_airport(self, airport_name):
        ''' returns index of an airport'''
        
        #get index of an airport
        for id_x,single_airport in enumerate(self.airports):
            if single_airport.name == airport_name:
                return id_x
            
        return -1 #TODO add condition to heck what happen in the result is -1
    
        
    #search engine
    def search(self, origin,destination,bags = 0,return_flight = False, time_cond = "1971-07-02T00:00:00"):
        ''' search over graph and return matches'''
        
        #get index of origin airport
        origin_id = self.get_id_of_airport(origin) 
        
        matches = []
        visited_connection = []
        visited_cities = []
        
        
        def grow(airport,visited_city,visited_connection,):
            ''' function that would be called recursiverly to search'''
            
            #copy all visited nonections and used flights
            v_cone = visited_connection.copy()
            v_city = visited_city.copy()
            
            
            if airport.name == destination:
                matches.append(v_cone)
                return
            
            
            v_city.append(airport)
            
            for single_connection in airport.connection:
                
                
                
                #if the airport was not visited yet  and if bags condition is met
                if single_connection.target_city not in v_city and int(single_connection.record['bags_allowed']) >= bags:

                    #check if the time condition is satiefied
                    if v_cone != []:
                        if is_time_in_interval(v_cone[-1].record['arrival'], single_connection.record['departure']):
                           
                            v_cone.append(single_connection)
                            grow(single_connection.target_city,v_city,v_cone)
                    else:
                        
                        #check if I want to look only for return flights
                        if return_flight:
                            if compare_two_time(single_connection.record['departure'],time_cond):
                   
                                v_cone.append(single_connection)
                                grow(single_connection.target_city,v_city,v_cone)

                        else:
                            v_cone.append(single_connection)
                            grow(single_connection.target_city,v_city,v_cone)
                        
        grow(self.airports[origin_id],visited_cities,visited_connection)
        return matches
        
        
        
        