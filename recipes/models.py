from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    STATUS_CHOICES = [
        ("favorite", "Favorite"),
        ("to_try", "To Try"),
        ("made_before", "Made Before"),
    ]

    name          = models.CharField(max_length=150)
    ingredients   = models.TextField(help_text="One ingredient per line")
    instructions  = models.TextField()
    cuisine_type  = models.CharField(max_length=80, blank=True)
    prep_time_min = models.PositiveSmallIntegerField(default=0)
    status        = models.CharField(max_length=12, choices=STATUS_CHOICES, default="to_try")
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_list")
