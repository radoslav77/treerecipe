from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

from .models import *


class registrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
       
        fields = ('title','recipe','method','outlet','image')


class SubRecipeForm(forms.ModelForm):


    class Meta:
        model = Sub_recipe
        fields = ('sub_title','title','sub_recipe','method')