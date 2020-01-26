from django.shortcuts import render, get_object_or_404

from rest_framework import generics
from .serializers import MealSerializer
from .models import Meal

class api_meal_generic(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer