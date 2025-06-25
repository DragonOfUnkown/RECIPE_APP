from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Recipe


class RecipeList(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "")
        status = self.request.GET.get("status", "")
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(ingredients__icontains=q) |
                Q(cuisine_type__icontains=q)
            )
        if status:
            qs = qs.filter(status=status)
        return qs


class RecipeCreate(CreateView):
    model = Recipe
    fields = "__all__"
    template_name = "recipes/recipe_form.html"


class RecipeUpdate(UpdateView):
    model = Recipe
    fields = "__all__"
    template_name = "recipes/recipe_form.html"


class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipe_list")
    template_name = "recipes/recipe_confirm_delete.html"
