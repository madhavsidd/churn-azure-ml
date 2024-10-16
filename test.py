import requests
import json

scoring_uri = ''

input_data = json.dumps({
    "data": [
        # Customer 1 
        [
    ]
})
headers = {'Content-Type': 'application/json'}
try:
    response = requests.post(scoring_uri, data=input_data, headers=headers)
    
    response.raise_for_status()
    
    print("Response from model:", response.json())
    
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")  
except Exception as e:
    print(f"An error occurred: {e}") 
