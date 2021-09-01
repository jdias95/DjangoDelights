from inventory.models import RecipeRequirement
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('ingredient/list', views.IngredientList.as_view(), name='ingredientlist'),
    path('ingredient/create', views.IngredientCreate.as_view(), name='ingredientcreate'),
    path('ingredient/delete/<pk>', views.IngredientDelete.as_view(), name='ingredientdelete'),
    path('ingredient/update/<pk>', views.IngredientUpdate.as_view(), name='ingredientupdate'),
    path('menuitem/list', views.MenuItemList.as_view(), name='menuitemlist'),
    path('menuitem/create', views.MenuItemCreate.as_view(), name='menuitemcreate'),
    path('reciperequirement/create/<id>', views.recipe_requirement_create, name='reciperequirementcreate'),
    path('reciperequirement/delete/<id>', views.recipe_requirement_delete, name='reciperequirementdelete'),
    path('purchase/list', views.PurchaseList.as_view(), name='purchaselist'),
    path('purchase/create', views.purchase_create, name='purchasecreate'),
    path('report', views.profit_report, name='report'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)