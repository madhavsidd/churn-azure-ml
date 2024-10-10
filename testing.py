import requests
import json

# Replace with the actual scoring URI of your deployed model
scoring_uri = 'http://cabd63a3-7549-47db-b56d-67c84f170c55.eastus2.azurecontainer.io/score'

# Encoded input data matching the expected feature order
input_data = json.dumps({
    "data": [
        # Customer 1 
        [2.273158691738958, 1.0345302279174904, -0.6540119291623984,
       0.22920887396235737, 0.3274383095561751, True, 102.6, 4009.2, 1, 0,
       1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0]
    ]
})
headers = {'Content-Type': 'application/json'}
try:
    # Send a POST request to the model's scoring URI
    response = requests.post(scoring_uri, data=input_data, headers=headers)
    
    # Raise an error if the request was unsuccessful
    response.raise_for_status()
    
    # Print the response from the model
    print("Response from model:", response.json())
    
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")  # Print the error
except Exception as e:
    print(f"An error occurred: {e}")  # Print any other exceptions
