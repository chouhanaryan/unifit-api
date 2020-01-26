from django.db import models

class Meal(models.Model):

    MEAL_CHOICES = [
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner')
    ]

    food_name = models.CharField(max_length=200)
    serving_qty = models.IntegerField(unique=False)
    nf_calories = models.FloatField(default=0)
    nf_total_fat = models.FloatField(default=0)
    nf_total_carbohydrate = models.FloatField(default=0)
    nf_protein = models.FloatField(default=0)
    choices =  models.CharField(max_length=20, choices=MEAL_CHOICES, default='B')

    def __str__(self):
        return self.food_name