# Python weekend entry task

** This is my solution to Entry task for python weekend organized by kiwi.com**
The purpose of this program is to find fligs between aiports. 

### Running the code
Code could be run using command line with these arguments:


#### Mandatory arguments
There are 3 mandatory arguments:

| Argument name | type    | Description              | Notes                        |
|---------------|---------|--------------------------|------------------------------|
| `path_data`   | string  | path to input csv file   | Mandatory                    |
| `origin`      | string  | Origin airport code      | Mandatory                    |
| `destination` | string  | Destination airport code | Mandatory                    |

#### Optional arguments
Optinal argument:

| Argument name | type    | Description              | Notes                        |
|---------------|---------|--------------------------|------------------------------|
| `bags`        | integer | Number of requested bags | Optional (defaults to 0)     |
| `return`      | boolean | Is it a return flight?   | Optional (defaults to false) |

Example of running the file: 
```bash
python -m solution example/example0.csv BTW REJ --bags=1
```
