from django import forms
from inventory.models import Ingredient, MenuItem, RecipeRequirement, Purchase

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = {"name", "quantity", "unit", "unit_price"}
    field_order = ["name", "quantity", "unit", "unit_price"]

class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = {"name", "quantity", "unit", "unit_price"}
    field_order = ["name", "quantity", "unit", "unit_price"]

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = {"title", "price"}
    field_order = ["title", "price"]

class RecipeRequirementCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = {"ingredient", "quantity"}
    field_order = ["ingredient", "quantity"]

class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = {"menu_item"}