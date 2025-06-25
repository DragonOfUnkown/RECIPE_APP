from django.urls import path
from . import views

urlpatterns = [
    path("", views.RecipeList.as_view(), name="recipe_list"),
    path("add/", views.RecipeCreate.as_view(), name="recipe_add"),
    path("<int:pk>/edit/", views.RecipeUpdate.as_view(), name="recipe_edit"),
    path("<int:pk>/delete/", views.RecipeDelete.as_view(), name="recipe_delete"),
]