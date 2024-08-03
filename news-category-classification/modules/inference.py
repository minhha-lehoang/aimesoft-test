import requests
import json

# Define the base URL for the API
base_url = 'http://localhost:5000'

# Make a prediction
def predict(text):
    url = f'{base_url}/predict'
    headers = {'Content-Type': 'application/json'}
    payload = {'text': text}

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        prediction = response.json()
        print(
            f"Prediction: {prediction['prediction']}, Probability: {prediction['probability']}")
    else:
        print(f"Failed to make prediction: {response.json()}")


if __name__ == '__main__':
    # Load the text from stdin
    text = input().strip()
    predict(text)