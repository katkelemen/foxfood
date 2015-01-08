from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    SI = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class RecipeIngredient(models.Model):
    amount = models.IntegerField(default = 1)
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)
    def __unicode__(self):
        return self.recipe.name + " " + self.ingredient.name