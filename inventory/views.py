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
    menu_item_id = obj.menu_item.id
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/reciperequirement/create/{}".format(menu_item_id))
    context["ingredient"] = obj
    context["menu_item_id"] = menu_item_id
    return render(request, "inventory/recipe_requirement_delete_form.html", context)

class PurchaseList(ListView):
    model = Purchase
    template_name = "inventory/purchases.html"

def purchase_create(request):
    context = {}
    form = PurchaseCreateForm(request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/purchase/list")
        
    context['form'] = form
    return render(request, "inventory/purchase_create_form.html", context)

def profit_report(request):     # variables for revenue and expenses decrease with changes made to model data
    total_revenue = 0
    total_expenses = 0
    purchases = Purchase.objects.all()
    for item in purchases:
        if item.menu_item != None:
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

