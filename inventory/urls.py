from inventory.models import RecipeRequirement
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('ingredient/list', views.ingredient_list, name='ingredientlist'),
    path('ingredient/create', views.ingredient_create, name='ingredientcreate'),
    path('ingredient/delete/<pk>', views.IngredientDelete.as_view(), name='ingredientdelete'),
    path('ingredient/update/<id>', views.ingredient_update, name='ingredientupdate'),
    path('menuitem/list', views.menu_item_list, name='menuitemlist'),
    path('menuitem/create', views.menu_item_create, name='menuitemcreate'),
    path('reciperequirement/create/<id>', views.recipe_requirement_create, name='reciperequirementcreate'),
    path('reciperequirement/delete/<id>', views.recipe_requirement_delete, name='reciperequirementdelete'),
    path('purchase/list', views.purchase_list, name='purchaselist'),
    path('purchase/create', views.purchase_create, name='purchasecreate'),
    path('report', views.profit_report, name='report'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)