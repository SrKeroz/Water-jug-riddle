# Flask
from flask import jsonify, request

# Directory
from . import api

# Water jug riddle
from app.water_jug_riddle.solved_water_jug_riddle import solve_water_jug_riddle
from app.water_jug_riddle.save_state import save_state_changes
from app.water_jug_riddle.validations import validations


@api.route('/solve', methods=['POST'])
def water_jug_riddle_api():
    """
    Solve the water jug riddle based on the provided parameters in the JSON request.
    
    Returns:
        If any of these parameters is missing, it returns a JSON response with an error message and a status code of 400.
        if the validation is not successful, it returns an message specifying the error and a status code of 400
        If the validation is successful, Finally, returns the 'result' as a JSON response with a status code of 200
    """

    # Check if all data necessary are provided in the JSON
    if 'x_gallon' not in request.json or 'y_gallon' not in request.json or 'water_to_measure' not in request.json:
        # if any data is missing return a error message
        return jsonify({'error': 'One or more parameters are missing.'}), 400
    else:
        # Get the data sent in the request body
        x_gallon = request.json['x_gallon']
        y_gallon = request.json['y_gallon']
        water_to_measure = request.json['water_to_measure']

        # validate that the data received is valid
        valid = validations(x_gallon, y_gallon, water_to_measure)

        if not valid[0]:
            # Return a error message as a JSON
            return jsonify({'message': valid[1]}), 400
        else:
            solution = solve_water_jug_riddle(x_gallon,y_gallon,water_to_measure)
            result = save_state_changes(solution)

            # Return the result as a JSON response
            return jsonify(result), 200 