# Meal Planner API

This project is a Django-based API for generating meal plans based on user preferences for protein goals, calorie goals, and the number of meals per day.


## Installation

1. Clone the repository:
```
git clone <repository-url>
cd backend
```

2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the development server:
```
python manage.py runserver
```
## Usage

The API provides an endpoint to generate meal plans based on user input. Send a POST request to `/meal-plan/` with JSON data containing the user's protein goal, calorie goal, and number of meals per day.

Example request:

```
{
"protein_goal": 100,
"calorie_goal": 2000,
"num_meals_per_day": 3
}
```

Example response:


```
{
  "Monday": ["Recipe 1", "Recipe 2", "Recipe 3"],
  "Tuesday": ["Recipe 4", "Recipe 5", "Recipe 6"],
  ...
}
```