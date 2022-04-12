import argparse

from graphDatabase import GraphDatabase
from flight import Flight
from airport import Airport
from dataExporter import DataExporter
from utils import *

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('path_data')
    parser.add_argument('origin')
    parser.add_argument('destination')
    parser.add_argument("--bags", "--bags", default=0)
    parser.add_argument("--return", "--return", default=False, action='store_true')

    args, unknown = parser.parse_known_args()
    
    if unknown != []:
        print("Invalid arguments")
        return -1

    args = vars(args)
    file =  args['path_data']
    from_destination = args['origin']
    goal_destination = args['destination']
    bag = int(args['bags'])
    return_f = args["return"]

    if from_destination == goal_destination:
        print("Invalid arguments")
        return -1

    try:
        csv_file = load_csv(file)
    except:
        print("Source file does not exists")
        return -1


    database = GraphDatabase(csv_file[0])
    database.load_data(csv_file[1:])

    matches = database.search(from_destination, goal_destination, bags = bag)

    if matches == []:
        print("No matches found")
        return 0

    new_data_exporter = DataExporter()

    one_way_flights_output = new_data_exporter.prepare_output_format_file(matches, 1, from_destination,
                                                                          goal_destination, bag)

    return_flights_output = []
    if return_f:
        matches_return = database.search(goal_destination, from_destination, bags = bag, return_flight = True, time_cond = matches[0][0].record['arrival'])

        return_flights_output = new_data_exporter.prepare_output_format_file(matches_return, 1, goal_destination,
                                                                             from_destination, bag)
    print(one_way_flights_output + return_flights_output)

    return 0
        

if __name__ == "__main__":
    main()
