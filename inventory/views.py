from inventory.forms import IngredientCreateForm, IngredientUpdateForm, MenuItemCreateForm, RecipeRequirementCreateForm, PurchaseCreateForm
from inventory.models import Ingredient, MenuItem, Purchase, RecipeRequirement
from django.shortcuts import render
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

class RecipeRequirementCreate(CreateView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_create_form.html'
    form_class = RecipeRequirementCreateForm

def recipe_requirement_create(request, **kwargs):
    context = {}
    menu_item = MenuItem.objects.get(pk=kwargs['pk'])
    recipe_requirements = RecipeRequirement.objects.all()
    print(menu_item)
    form = RecipeRequirementCreateForm(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "inventory/recipe_requirement_create_form.html", context)

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

