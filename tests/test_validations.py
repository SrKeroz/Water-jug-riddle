import json
from main import app

app.testing = True
client = app.test_client()

# This variable represents the API path that is used to perform the POST request.
path = '/api/solve'

def test_validate_integers_successful():
    # Prepare test data
    json_data = {
        'x_gallon': 10,
        'y_gallon': 2,
        'water_to_measure': 4
    }
    # Make the POST request
    response = client.post(path, json=json_data)
    # Verificar el código de estado y el mensaje de respuesta
    assert response.status_code == 200

def test_validate_decimal_failure():
    # Prepare test data with a decimal parameter
    json_data = {
        'x_gallon': 1.5,
        'y_gallon': 2,
        'water_to_measure': 4
    }
    # Make the POST request
    response = client.post(path, json=json_data)
    # Verificar el código de estado y el mensaje de respuesta
    assert response.status_code == 400
    json_response = json.loads(response.data)
    assert json_response['message'] == "Values can't be decimals or fractions"

def test_validate_string_failure():
    # Prepare test data with a string parameter
    json_data = {
        'x_gallon': "abc",
        'y_gallon': 2,
        'water_to_measure': 4
    }
    # Make the POST request
    response = client.post(path, json=json_data)
    # Check status code and response message
    assert response.status_code == 400
    json_response = json.loads(response.data)
    assert json_response['message'] == "Values can't be signs or letters"

def test_validate_parameter_with_zero_value_failure():
    # Prepare test data with a parameter less than 0 or equal that 0
    json_data = {
        'x_gallon': 0,
        'y_gallon': 2,
        'water_to_measure': 4
    }
    # Make the POST request
    response = client.post(path, json=json_data)
    # Check status code and response message
    assert response.status_code == 400
    json_response = json.loads(response.data)
    assert json_response['message'] == "Values must be greater than 0"


def test_validate_z_greater_than_x_and_y_failure():
    # Prepare test data with n3 parameter greater than n1 and n2
    json_data = {
        'x_gallon': 10,
        'y_gallon': 2,
        'water_to_measure': 400
    }
    # Make the POST request
    response = client.post(path, json=json_data)
    # Check status code and response message
    assert response.status_code == 400
    json_response = json.loads(response.data)
    assert json_response['message'] == "Water to measure can't be greater than x_gallon and y_gallon"
