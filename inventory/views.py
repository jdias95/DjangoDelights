from typing import List

from django.http.response import HttpResponseRedirect
from inventory.forms import IngredientCreateForm, IngredientUpdateForm, MenuItemCreateForm, RecipeRequirementCreateForm, PurchaseCreateForm
from inventory.models import Ingredient, MenuItem, Purchase, RecipeRequirement
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, "inventory/home.html")

class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/inventory.html"

class IngredientCreate(CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_create_form.html'
    form_class = IngredientCreateForm

class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_update_form.html'
    form_class = IngredientUpdateForm
    success_url = reverse_lazy("ingredientlist")

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"
    success_url = reverse_lazy("ingredientlist")

class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/menu.html"

class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = 'inventory/menu_item_create_form.html'
    form_class = MenuItemCreateForm

def recipe_requirement_create(request, id):
    context = {}
    menu_item = MenuItem.objects.get(id=id)
    recipe_ingredients = RecipeRequirement.objects.filter(menu_item=menu_item)
    print(id)
    print(recipe_ingredients)
    form = RecipeRequirementCreateForm(request.POST)
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.menu_item = menu_item
        recipe.save()
    context['form'] = form
    context['menu_item'] = menu_item
    context['recipe_ingredients'] = recipe_ingredients
    return render(request, "inventory/recipe_requirement_create_form.html", context)

def recipe_requirement_delete(request, id):
    context = {}
    obj = get_object_or_404(RecipeRequirement, id=id)
    print(obj)
    print(id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    context["ingredient"] = obj
    return render(request, "inventory/recipe_requirement_delete_form.html", context)

class RecipeRequirementDelete(DeleteView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirement_delete_form.html"
    success_url = reverse_lazy("reciperequirementcreate", args=[id])

class PurchaseList(ListView):
    model = Purchase
    template_name = "inventory/purchases.html"

class PurchaseCreate(CreateView):
    model = Purchase
    template_name = 'inventory/purchase_create_form.html'
    form_class = PurchaseCreateForm

def profit_report(request):
    total_revenue = 0
    total_expenses = 0
    purchases = Purchase.objects.all()
    for item in purchases:
        item_id = item.menu_item.id
        menu = MenuItem.objects.get(pk=item_id)
        total_revenue += menu.price

    ingredients = Ingredient.objects.all()
    for item in ingredients:
        total_expenses += (item.unit_price * item.quantity)

    total = total_revenue - total_expenses
    total_profit = None
    if total >= 0:
        total_profit = total
    else:
        total_profit = total * -1

    context = {
        "total_revenue": total_revenue,
        "total_expenses": total_expenses,
        "total": total,
        "total_profit": total_profit
    }
    return render(request, "inventory/report.html", context)

