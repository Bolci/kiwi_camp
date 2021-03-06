from flight import Flight
from airport import Airport
from utils import *
import time

class GraphDatabase():
    def __init__(self, attributes):
        self.attributes = attributes
        self.airports = []

    def add_record(self, record):
        ''' add single record to database'''

        #record = dict(zip(self.attributes,single_record))
        record = {k: v for k,v in zip(self.attributes, record)}

        #initial variables
        saved_id_of_destination = -1
        saved_id_of_origin = -1
        origin_found = False
        destination_found = False

        #check if airport exists
        for id_x, single_airport in enumerate(self.airports):

            #check for destination airport and save its index if found
            if single_airport.name == record['destination']:
                saved_id_of_destination = id_x
                destination_found = True

                if origin_found:
                    break

            #check if the city is in the databaae
            if single_airport.name == record['origin']:
                saved_id_of_origin = id_x
                origin_found = True

                if destination_found:
                    break

        new_flight = Flight(record)

        #process destination
        if not destination_found:
            self.airports.append(Airport(record['destination']))

        new_flight.add_target_city(self.airports[saved_id_of_destination])

        #process origin
        if not origin_found:
            self.airports.append(Airport(record['origin']))

        self.airports[saved_id_of_origin].add_flight(new_flight)

    def load_data(self, raw_data):
        ''' load list of lists of data'''
        for data_line in raw_data:
            self.add_record(data_line)

    def get_id_of_airport(self, airport_name):
        ''' returns index of an airport'''

        #get index of an airport
        for id_x,single_airport in enumerate(self.airports):
            if single_airport.name == airport_name:
                return id_x

        return -1

    def search(self, origin, destination, bags = 0, return_flight = False, time_cond = "1971-07-02T00:00:00"):
        ''' search over graph and return matches'''

        #get index of origin airport
        origin_id = self.get_id_of_airport(origin)


        if origin_id == -1:
            return []

        matches = []
        used_flights_global = []
        visited_cities_global = []

        def grow(airport, visited_cities, used_flights):
            ''' function that would be called recursiverly to search'''

            #copy all visited nonections and used flights


            if airport.name == destination:
                matches.append(used_flights)
                return

            visited_cities_copy = visited_cities.copy()
            visited_cities_copy.append(airport)


            for single_flight in airport.flights:
                if single_flight.target_city not in visited_cities_copy and int(single_flight.record['bags_allowed']) >= bags:

                    if used_flights != []:
                        if not is_time_in_interval(used_flights[-1].record['arrival'], single_flight.record['departure'], [1,6]):
                            continue
                        elif return_flight and not is_time_bigger(single_flight.record['departure'],time_cond):
                            continue

                    used_flights_copy = used_flights.copy()
                    used_flights_copy.append(single_flight)
                    grow(single_flight.target_city, visited_cities_copy, used_flights_copy)


        grow(self.airports[origin_id], visited_cities_global, used_flights_global)

        return matches



