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
    path('reciperequirement/create/<pk>', views.RecipeRequirementCreate.as_view(), name='reciperequirementcreate'),
    path('purchase/list', views.PurchaseList.as_view(), name='purchaselist'),
    path('purchase/create', views.PurchaseCreate.as_view(), name='purchasecreate'),
    path('report', views.profit_report, name='report'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)