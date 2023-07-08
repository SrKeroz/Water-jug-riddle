# Water Jug Riddle Solver API

This API allows you to solve the water jug riddle, The route expects a `JSON` payload with three parameters: `x_gallon`, `y_gallon`, and `water_to_measure`. It first checks if all three parameters are present in the JSON. If any of them is missing, it returns a JSON response with an error message and a status code of `400 (Bad Request)`.

If all the parameters are present, the code proceeds to extract the values of `x_gallon`, `y_gallon`, and `water_to_measure` from the `JSON` payload. It then performs validation on the received data, then checks if the values meet certain criteria:

1. the values must be greater than 0
2. values cannot be strings or signs
3. Values must be integers, not fractions or decimals
4. `water_to_measure` can't be greater than `x_gallon` or `y_gallon`

If the validation is successful, finally, the code returns the result as a `JSON` response with a status code of `200 (OK)`.

## Installation

1. Clone this repository: `git clone https://github.com/SrKeroz/Water-jug-riddle.git`
2. Navigate to the project directory: `cd Water-jug-riddle`
3. Install dependencies: `python -m pip install -r requirements.txt`

## Usage

To use the Water Jug Riddle Solver API, follow these steps:

1. Start the API server: `python main.py`
2. Send a POST request to the following endpoint: `http://localhost:5000/api/solve`
3. Include the following parameters in the request body:
   - `x_gallon`: The capacity of the X-gallon jug.
   - `y_gallon`: The capacity of the Y-gallon jug.
   - `water_to_measure`: The amount of water to measure.
4. the API will validate that the data sent is correct.
5. The API will return a JSON response with the solution to the riddle, if found.

Example cURL request:

```shell
curl -X POST -H "Content-Type: application/json" -d '{
  "x_gallon": 8,
  "y_gallon": 2,
  "water_to_measure": 4
}' http://localhost:5000/api/solve
```

Response
```shell
[
  [
    "Fill X",
    "(X: 8, Y: 0)"
  ],
  [
    "Transfer X to Y",
    "(X: 6, Y: 2)"
  ],
  [
    "Empty Y",
    "(X: 6, Y: 0)"
  ],
  [
    "Transfer X to Y",
    "(X: 4, Y: 2)"
  ]
]
```
## Showing Solutions

### solution to exercise 1

- `x_gallon` = 9  
- `y_gallon` = 11  
- `water_to_measure` = 4  

Response
```shell
[
  [
    "Fill Y",
    "(X: 0, Y: 11)"
  ],
  [
    "Transfer Y to X",
    "(X: 9, Y: 2)"
  ],
  [
    "Empty X",
    "(X: 0, Y: 2)"
  ],
  [
    "Transfer Y to X",
    "(X: 2, Y: 0)"
  ],
  [
    "Fill Y",
    "(X: 2, Y: 11)"
  ],
  [
    "Transfer Y to X",
    "(X: 9, Y: 4)"
  ]
]
```
### solution to exercise 2 

- `x_gallon` = 5  
- `y_gallon` = 3  
- `water_to_measure` = 4  

Response
```shell
[
  [
    "Fill X",
    "(X: 5, Y: 0)"
  ],
  [
    "Transfer X to Y",
    "(X: 2, Y: 3)"
  ],
  [
    "Empty Y",
    "(X: 2, Y: 0)"
  ],
  [
    "Transfer X to Y",
    "(X: 0, Y: 2)"
  ],
  [
    "Fill X",
    "(X: 5, Y: 2)"
  ],
  [
    "Transfer X to Y",
    "(X: 4, Y: 3)"
  ]
]
```
### solution to exercise 3  

- `x_gallon` = 20  
- `y_gallon` = 120  
- `water_to_measure` = 400  


Response
```shell
{
  "message": "Z can't be greater than X and Y"
}
```

## Running Tests

To run the tests for the Water Jug Riddle Solver API, follow these steps:

1. Navigate to the `Water-jug-riddle/tests` directory: `cd Water-jug-riddle/tests`
2. Execute the following command to run the tests using pytest: `pytest`

Make sure you have the necessary dependencies installed before running the tests. You can install the required dependencies by following the installation instructions mentioned earlier in this README.

Running the tests will help ensure the correctness and reliability of the API's functionality. If any tests fail, it indicates a potential issue with the implementation that needs to be addressed.
