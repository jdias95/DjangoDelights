from django.db import models
from datetime import datetime

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)          # attributes listed incorrectly on form pages
    quantity = models.IntegerField()
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

    def __str__(self):
        return self.name + " quantity: " + str(self.quantity) + ",\n" + "price per " + self.unit + ": $" + str(format(self.unit_price, '.2f')) if (self.unit != 'None') else self.name + " quantity: " + str(self.quantity) + ",\n" + "price per: $" + str(format(self.unit_price, '.2f'))

    def get_absolute_url(self):
        return "/ingredient/list"

class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return self.title + " costs $" + str(format(self.price, '.2f')) 
    
    def get_absolute_url(self):
        return "/menuitem/list"

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return str(self.menu_item) + " and requires " + str(self.quantity) + " of its unit of " + str(self.ingredient)

    def get_absolute_url(self):
        return "/menuitem/list"

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.menu_item) + " purchased at " + str(self.timestamp)

    def get_absolute_url(self):
        return "/purchase/list"