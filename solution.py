import argparse

def main(args):    
    
    #parsing input arguments
    if not args.path_data or not args.from_dest or not args.goal_dest:
        print("Invalid arguments")
        return -1
    
    #csv_file = load_csv(args.path_dat)
    
    
    

if __name__ == "__main__":
    #create instance of argument parser
    parser = argparse.ArgumentParser()
    
    #add valid arguments
    parser.add_argument('path_data')
    parser.add_argument('from_dest')
    parser.add_argument('goal_dest')
    parser.add_argument("--bags", "--bags", help="show program version", default=0)
    parser.add_argument("--return", "--return", help="show program version", default=False)

    args = parser.parse_args()
    print(args)
    
    main(args)
    
    