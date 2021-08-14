from inventory.models import Ingredient, MenuItem, Purchase
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import DeleteView

# Create your views here.
def home(request):
    return render(request, "inventory/home.html")

class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/inventory.html"

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"

class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/menu.html"

class PurchaseList(ListView):
    model = Purchase
    template_name = "inventory/purchases.html"

def profit_report(request):
    return render(request, "inventory/report.html")

