from django.contrib import admin
from django.contrib.auth.models import User

from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=("id","username","email","password")

class RecipeAdmin(admin.ModelAdmin):
    list_display=('id','title','recipe','method','outlet', 'image')
admin.site.register(Recipe,RecipeAdmin)

class HandoverAdmin(admin.ModelAdmin):
    list_display=('id','user','msg', 'date')
admin.site.register(Handover,HandoverAdmin)

class Sub_recipeAdmin(admin.ModelAdmin):
    list_display = ('id','title','sub_title','sub_recipe', 'method')

admin.site.register(Sub_recipe,Sub_recipeAdmin)
