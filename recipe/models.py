from django.db import models

# Create your models here.


class Recipe(models.Model):
    OUTLET = (
        ('The Nest', 'Afternoon Tea'),
        ('Madara', 'Madara'),
        ('Pizza Mozzo', 'Banqueting'),
        ('breakfast', 'Breakfast'),
        ('Room Service', 'Room Service'),
        ('Recipes', 'Recipes'),
        ('Amenities', 'Amenities')
    )
    title = models.CharField(max_length=300)
    recipe = models.TextField(max_length=2000)
    method = models.TextField(max_length=2000)
    image = models.URLField(default=None, null=True)
    outlet = models.CharField(max_length=100, choices=OUTLET)
    #archived = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']


class Sub_recipe(models.Model):
    sub_title = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='base_title')
    title = models.CharField(max_length=300)
    sub_recipe = models.TextField(max_length=2000)
    method = models.TextField(max_length=2000)
    #archived = models.BooleanField(default=False)

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
