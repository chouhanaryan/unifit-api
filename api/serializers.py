from rest_framework import serializers
from .models import Meal

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        # fields = ['food_name', 'serving_qty', 'nf_calories', 'nf_total_fat', 'nf_total_carbohydrate', 'nf_protein', 'choices']
        fields = '__all__'