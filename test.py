import requests

# Define the data to send in the POST request
data = {
    'protein_goal': 100,  # Replace with the user's protein goal
    'calorie_goal': 2000,  # Replace with the user's calorie goal
    'num_meals_per_day': 3  # Replace with the number of meals per day
}

# Make a POST request to the API endpoint
response = requests.post('http://127.0.0.1:8000/meal-plan/', json=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response JSON data
    print(response.json())
else:
    # Print the error message if the request was not successful
    print(f"Error: {response.status_code} - {response.text}")
