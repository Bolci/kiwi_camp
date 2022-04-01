from collections import defaultdict
from operator import itemgetter


class DataBank():
    def __init__(self,all_raw_data):
        self.attributes = []
        self._basic_graph = defaultdict(set)
        self._graph = defaultdict(list)
        self._graph_ids = defaultdict(list)
        self.database = defaultdict(dict)
        self.data_id = 0
        
        self.get_graph_from_raw_data(all_raw_data)
        
        
    def connection_exist(self, connection):
        ''' check if the connection exists'''
        
        if not connection[0] in self._graph:
            return False
        else:
            if connection[1] not in self._graph[connection[0]]:
                return False
        return True
            
        
    
    def get_matches(self,from_place,to_place):
        matches = self._graph[from_place]
 
        index_pos = 0
        indexes = []
        
        while index_pos <= self.data_id:
            try:
                index_pos = matches.index(to_place, index_pos)
            except ValueError:
                break
            indexes.append(index_pos)
            index_pos += 1
        
        
        #return itemgetter(*indexes)(self.all_data_raw)
        selected_database = list(map(lambda x: self.database[x], indexes))
        
        return selected_database
        
    
    def add_path(self, flight):
        '''add path to graph from raw data'''
        
        place_a = flight[1]
        place_b = flight[2]
        #if not self.connection_exist((place_a,place_b)):
        self._graph[place_a].append(place_b)
        self._graph_ids[place_a].append(self.data_id)
        self._basic_graph[place_a].add(place_b)
        
        self.database[self.data_id] = dict(zip(self.attributes,flight))
        
        self.data_id += 1
        
    
    def get_graph_from_raw_data(self,all_data_raw):
        ''' take list of raw data and turn it into graph representation'''
        self.attributes = all_data_raw[0]
        #iterate over every flight
        list(map(self.add_path,all_data_raw[1:]))