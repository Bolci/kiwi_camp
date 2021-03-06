import argparse

from graphDatabase import Graph_Database
from flight import Conection
from airport import Airport
from dataExporter import DataExporter
from utils import *

def main():
    #create instance of argument parser
    parser = argparse.ArgumentParser()
    
    #add valid arguments
    
    
    parser.add_argument('path_data')
    parser.add_argument('from_dest')
    parser.add_argument('goal_dest')
    parser.add_argument("--bags", "--bags", help="number of required bags", default=0)
    parser.add_argument("--return", "--return", help="is return flight required", default=False, action='store_true')

    
    #parsing input arguments
    args, unknown = parser.parse_known_args()
    
    if unknown != []:
        print("Invalid arguments")
        return -1
    
    #get args
    args = vars(args)
    file =  args['path_data']
    from_dest = args['from_dest']
    goal_dest = args['goal_dest']
    bag = int(args['bags'])
    return_f = args["return"]
    
    #check if from and goal dest are not the same
    if from_dest == goal_dest:
        print("Invalid arguments")
        return -1

    #load database
    try:
        csv_file = load_csv(file)
    except:
        print("Source file does not exists")
        return -1

    #prepare database
    database = Graph_Database(csv_file[0])
    database.load_data(csv_file[1:])
    
    #search in database
    mat = database.search(from_dest,goal_dest,bags=bag)
   
    if mat == []:
        print("No matches found")
        return 0
    #export data
    NewDataExporter = DataExporter()
    
    print("Printing flights")
    NewDataExporter.save_file(mat,1,from_dest,goal_dest,bag)
    
    #get return flight
    if return_f:
        mat_return = database.search(goal_dest,from_dest,bags=bag,return_flight = True, time_cond = mat[0][0].record['arrival'])
        print("Printing return flights")
        NewDataExporter.save_file(mat_return,1,goal_dest,from_dest,bag)
    
    
    return 0
        

if __name__ == "__main__":
    main()
