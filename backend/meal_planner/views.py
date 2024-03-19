# views.py
import random
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers


# from .serializers import MealPlanRequestSerializer
# from .meal_planner_logic import generate_meal_plans  # Assuming you have a function to generate meal plans

def get_recipes(protein_goal, calorie_goal, num_meals):
    # Make API request to fetch recipes based on user preferences
    # Replace 'API_KEY' with your actual API key
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": "34d9979a85c74ffd8ade884a435520f9",
        "diet": "balanced",
        "minProtein": protein_goal,
        "maxCalories": calorie_goal,
        "number": num_meals * 7  # Fetch enough recipes for a week
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Extract recipe information from the API response
    recipes = [recipe["title"] for recipe in data["results"]]
    return recipes

# Function to generate a week's worth of meal plans
def generate_meal_plans(protein_goal, calorie_goal, num_meals_per_day):
    # Fetch recipes based on user preferences
    recipes = get_recipes(protein_goal, calorie_goal, num_meals_per_day)

    # Generate meal plans for each day of the week
    meal_plans = {}
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days_of_week:
        meals = random.sample(recipes, num_meals_per_day)
        meal_plans[day] = meals

    return meal_plans


class MealPlanRequestSerializer(serializers.Serializer):
    protein_goal = serializers.FloatField()
    calorie_goal = serializers.FloatField()
    num_meals_per_day = serializers.IntegerField()




class MealPlanAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MealPlanRequestSerializer(data=request.data)
        if serializer.is_valid():
            protein_goal = serializer.validated_data['protein_goal']
            calorie_goal = serializer.validated_data['calorie_goal']
            num_meals_per_day = serializer.validated_data['num_meals_per_day']
            meal_plan = generate_meal_plans(protein_goal, calorie_goal, num_meals_per_day)
            return Response(meal_plan)
        return Response(serializer.errors, status=400)
