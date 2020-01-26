from .views import api_meal_generic
from django.urls import path

urlpatterns = [
    path('', api_meal_generic.as_view(), name='api_meal_generic')
]