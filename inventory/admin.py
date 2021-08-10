from django.contrib import admin
from .models import Ingredient, MenuItems, RecipeRequirement, Purchase
# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItems)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)