# serializers.py
from rest_framework import serializers

class MealPlanRequestSerializer(serializers.Serializer):
    protein_goal = serializers.FloatField()
    calorie_goal = serializers.FloatField()
    num_meals_per_day = serializers.IntegerField()
