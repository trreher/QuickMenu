from django.contrib import admin
from .models import Recipe, Ingredient, MenuOffering, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        RecipeIngredientInline,
    ]

class IngredientAdmin(admin.ModelAdmin):
    inlines = [
        RecipeIngredientInline,
    ]


# Register your models here.
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(MenuOffering)
#admin.site.register(RecipeIngredient)