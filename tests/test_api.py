# python
import json
import time

# directory
from main import app

app.testing = True
client = app.test_client()

# This variable represents the API path that is used to perform the POST request.
path = '/api/solve'


def test_all_valid_parameter():
    # Prepare test data with all valid parameters
    json_data = {
        'x_gallon': 10,
        'y_gallon': 2,
        'water_to_measure': 4
    }

    # Make a POST request
    response = client.post(path, json=json_data)
    #Check status code
    assert response.status_code == 200

def test_missing_parameters():
    # Prepare test data with a missing parameter
    json_data = {
        'x_gallon': 10,
        'water_to_measure': 4
    }
    # Make a POST request
    response = client.post(path, json=json_data)
    # Check status code and response message
    assert response.status_code == 400
    json_response = json.loads(response.data)
    assert json_response['error'] == 'One or more parameters are missing.'

def test_performance():
    # Prepare test data with all valid parameters
    json_data = {
        'x_gallon': 10,
        'y_gallon': 2,
        'water_to_measure': 4
    }

    num_requests = 1000
    response_times = []

    for _ in range(num_requests):
        start_time = time.time()
        response = client.post(path, json=json_data)
        assert response.status_code == 200
        end_time = time.time()
        elapsed_time = end_time - start_time
        response_times.append(elapsed_time)

    average_time = sum(response_times) / num_requests

    # Check that the average response time is acceptable
    assert average_time < 0.1 

def test_multiple_requests():
    # Prepare test data with all valid parameters
    json_data1 = {
        'x_gallon': 10,
        'y_gallon': 2,
        'water_to_measure': 4
    }

    response1 = client.post(path, json=json_data1)
    assert response1.status_code == 200
    data1 = json.loads(response1.data)
    # Prepare test data with all valid parameters
    json_data2 = {
        'x_gallon': 9,
        'y_gallon': 11,
        'water_to_measure': 4
    }

    response2 = client.post(path, json=json_data2)
    assert response2.status_code == 200
    data2 = json.loads(response2.data)