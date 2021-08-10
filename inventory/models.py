from django.db import models

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    MEASUREMENTS = [
        ('tsp', 'teaspoon'),
        ('tbsp', 'tablespoon'),
        ('c', 'cup'),
        ('pt', 'pint'),
        ('qt', 'quart'),
        ('gal', 'gallon'),
        ('lb', 'pound')
    ]
    unit = models.CharField(max_length=10, choices=MEASUREMENTS)
    unit_price = models.FloatField()

    def __str__(self):
        return self.name + " quantity: " + str(self.quantity) + "\n" + "price per " + self.unit + ": $" + str(self.unit_price)

class MenuItems(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return self.title + " costs $" + self.price

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return "Menu Item with ID of " + str(self.menu_item) + " requires " + str(self.quantity) + " of its unit of the ingredient with the ID " + str(self.ingredient)

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.menu_item + " purchased at " + str(self.timestamp)