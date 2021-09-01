from django.db import models
from datetime import datetime
from django.db.models.deletion import CASCADE

# Create your models here.
class Ingredient(models.Model):                         # want model data to be viewed relative to each account
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    previous_quantity = models.IntegerField(default=0)
    MEASUREMENTS = [
        ('tsp', 'teaspoon'),
        ('tbsp', 'tablespoon'),
        ('g', 'grams'),
        ('oz', 'ounce'),
        ('c', 'cup'),
        ('pt', 'pint'),
        ('qt', 'quart'),
        ('gal', 'gallon'),
        ('lb', 'pound'),
        ('None', None)
    ]
    unit = models.CharField(max_length=10, choices=MEASUREMENTS)
    unit_price = models.DecimalField(max_digits=30, decimal_places=2)
    expense = models.DecimalField(max_digits=30, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/ingredient/list"

class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/menuitem/list"

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return str(self.ingredient) + " | " + str(self.quantity)

    def get_absolute_url(self):
        return "/menuitem/list"

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.menu_item) + " purchased at " + str(self.timestamp)

    def get_absolute_url(self):
        return "/purchase/list"