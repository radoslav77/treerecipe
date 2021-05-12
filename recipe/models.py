from django.db import models

# Create your models here.


class Recipe(models.Model):
    OUTLET=(
        ('The Nest', 'The Nest'),
        ('Madara', 'Madara'),
        ('Pizza Mozzo', 'Pizza Mozzo'),
        ('breakfast', 'Breakfast'),
        ('Room Service', 'Room Service'),
        ('Recipes', 'Recipes')
    )
    title = models.CharField(max_length=300)
    recipe = models.TextField(max_length=2000)
    method = models.TextField(max_length=2000)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    outlet = models.CharField(max_length=100, choices=OUTLET)

    def __str__(self):
        return f'{self.title}'

class Sub_recipe(models.Model):
    sub_title = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='base_title')
    title = models.CharField(max_length=300)
    sub_recipe = models.TextField(max_length=2000)
    method = models.TextField(max_length=2000)

    def __str__(self):
        return f'{self.title}: {self.sub_title}'


    class Meta:
        ordering = ['title']

class Handover(models.Model):
    user = models.CharField(max_length=200)
    msg = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.msg},{self.date}'

