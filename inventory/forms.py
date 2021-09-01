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
        fields = {"quantity"}

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

    def clean(self):
        menu_item = self.cleaned_data.get('menu_item')
        recipe = RecipeRequirement.objects.filter(menu_item=menu_item)
        for r in recipe:
            inventory_stock = r.ingredient.quantity - r.quantity
            if inventory_stock < 0:
                raise forms.ValidationError("Not enough ingredients in stock.")
        for r in recipe:
            r.ingredient.quantity -= r.quantity
            r.ingredient.save(update_fields=["quantity"])