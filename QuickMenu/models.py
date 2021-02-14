from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from decimal import Decimal

class Ingredient(models.Model):
    name = models.CharField(max_length=50,blank=False, null=False, default=' ')
    description = models.CharField(max_length=50, blank=True, null=True,default=' ')
    purchaseAmount = models.DecimalField(max_digits=10, decimal_places=3, null=True, default=Decimal(0))
    lastPurchasePrice = models.DecimalField(max_digits=10, decimal_places=3, null=True, default=Decimal(0))
    lastPurchaseDate = models.DateTimeField(auto_now_add=True)
    measurementType = models.CharField(max_length=10, default='g')
    lastUpdate = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredients_detail', args=[str(self.id)])

class Recipe(models.Model):

    name = models.CharField(max_length=50,blank=False, null=False, default=' ')
    description = models.CharField(max_length=50, blank=True, null=True,default=' ')
    instructions = models.CharField(max_length=50, blank=True, null=True,default=' ')
    servings = models.IntegerField(default='1')
    lastUpdate = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])

class MenuOffering(models.Model):
    name = models.CharField(max_length=50,blank=False, null=False, default=' ')
    offerPrice = models.DecimalField(max_digits=10, decimal_places=3, null=True, default=Decimal(0))
    offeringStart = models.DateTimeField(auto_now_add=True)
    offeringEnd = models.DateTimeField(auto_now_add=True)
    quantiySold = models.IntegerField(default='0')
    lastUpdate = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe',
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu_offering', args=[str(self.id)])

class RecipeIngredient(models.Model):

    amount = models.DecimalField(max_digits=10, decimal_places=3, null=True, default=Decimal(0))
    description = models.CharField(max_length=50, blank=True, null=True,default=' ')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ri_recipe',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ri_ingredient',
    )

    def __str__(self):
        return self.recipe.name +"-"+self.ingredient.name

    def get_absolute_url(self):
        return reverse('recipe_ingredient')
