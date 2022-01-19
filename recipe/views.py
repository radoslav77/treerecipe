from django.db import reset_queries
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
import requests
import datetime
from django.urls import reverse


from .forms import *

from .models import *
# Create your views here.


def index(request):
    user = request.user
    return render(request, 'recipe/start.html', {
        'user': user
    })


def madara(request):
    if request.user.is_authenticated:
        data = Recipe.objects.all().order_by('title')
        outlets = []
        for outlet in data:
            if outlet.outlet == 'Madara':

                outlets.append(outlet)

        return render(request, 'recipe/recipe.html', {
            'out': outlets
        })
    else:
        msg = 'Please Log in to Gain accses!'
        return render(request, 'recipe/base.html', {
            'msg': msg
        })


def pizza(request):
    if request.user.is_authenticated:
        data = Recipe.objects.all().order_by('title')
        outlets = []
        for outlet in data:
            if outlet.outlet == 'Pizza Mozzo':

                outlets.append(outlet)

        return render(request, 'recipe/recipe.html', {
            'out': outlets
        })
    else:
        msg = 'Please Log in to Gain accses!'
        return render(request, 'recipe/base.html', {
            'msg': msg
        })


def breakfast(request):
    if request.user.is_authenticated:
        data = Recipe.objects.all().order_by('title')
        outlets = []
        for outlet in data:
            if outlet.outlet == 'breakfast':

                outlets.append(outlet)

        return render(request, 'recipe/recipe.html', {
            'out': outlets
        })
    else:
        msg = 'Please Log in to Gain accses!'
        return render(request, 'recipe/base.html', {
            'msg': msg
        })


def nest(request):
    if request.user.is_authenticated:
        data = Recipe.objects.all().order_by('title')
        outlets = []
        current = []
        for outlet in data:
            if outlet.outlet == 'The Nest':

                outlets.append(outlet)
                # saves only the currant recipe
        for a in outlets:
            data = Recipe.objects.filter(
                title__icontains='Old').order_by('title')
            if not a in data:
                current.append(a)
        return render(request, 'recipe/recipe.html', {
            'out': current
        })
    else:
        msg = 'Please Log in to Gain accses!'
        return render(request, 'recipe/base.html', {
            'msg': msg
        })


def archived(request):
    if request.user.is_authenticated:
        data = Recipe.objects.filter(
            title__icontains='Old').order_by('title')
        data_recipe = []
        for d in data:

            if d in data:
                data_recipe.append(d)
        print(data_recipe)
        return render(request, 'recipe/recipe.html', {
            'out': data_recipe
        })


def amenities(request):
    if request.user.is_authenticated:
        data = Recipe.objects.all().order_by('title')
        outlets = []
        for outlet in data:
            if outlet.outlet == 'Amenities':

                outlets.append(outlet)

        return render(request, 'recipe/recipe.html', {
            'out': outlets
        })
    else:
        msg = 'Please Log in to Gain accses!'
        return render(request, 'recipe/base.html', {
            'msg': msg
        })


def recipes(request):
    if request.user.is_authenticated:
        data = Recipe.objects.all().order_by('title')
        outlets = []
        for outlet in data:
            if outlet.outlet == 'Recipes':

                outlets.append(outlet)

        return render(request, 'recipe/recipe.html', {
            'out': outlets
        })
    else:
        msg = 'Please Log in to Gain accses!'
        return render(request, 'recipe/base.html', {
            'msg': msg
        })


def recipe(request, title):
    data = Recipe.objects.filter(title=title)

    ing = []
    ingr = []
    for i in data:
        ingr = i.recipe.split(',')
        ing.append(ingr[0:-1])

        for j in ing:
            i = j[0][0]
            ingr.append(i[0:-1])

    sub_data = Sub_recipe.objects.filter(sub_title=data[0])
    title = []

    for t in sub_data:
        title.append(t)

    return render(request, 'recipe/index.html', {
        'data': data,
        'ing': ingr,
        'subrecipe': title,

    })


def subrecipe(request, title, id):
    data = Sub_recipe.objects.filter(title=title)

    ing = []
    ingr = []
    for i in data:
        ingr = i.sub_recipe.split(',')
        ing.append(ingr)
        for j in ing:
            i = j[0][0]
            ingr.append(i[0:-1])

    return render(request, 'recipe/subindex.html', {

        'data': data[0],
        'ing': ingr,

    })


def room_service(request):
    if request.user.is_authenticated:
        data = Recipe.objects.all().order_by('title')
        outlets = []
        for outlet in data:
            if outlet.outlet == 'Room Service':

                outlets.append(outlet)
        print(outlets)
        return render(request, 'recipe/recipe.html', {
            'out': outlets
        })
    else:
        msg = 'Please Log in to Gain accses!'
        return render(request, 'recipe/base.html', {
            'msg': msg
        })


def input(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid:
            data = form.save(commit=False)
            data.save()

            return redirect('index')

    return render(request, 'recipe/input.html', {
        'form': RecipeForm()
    })


def inputsub(request):
    if request.method == 'POST':
        form = SubRecipeForm(request.POST)

        if form.is_valid:
            data = form.save(commit=False)
            data.save()
            return redirect('index')

    return render(request, 'recipe/inputsub.html', {
        'form': SubRecipeForm()
    })


def handover(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            msg = request.POST['msg']
            user = request.user
            if not msg:
                message = 'You need to type-in Your Message!'
                return render(request, 'recipe/handover.html', {
                    'message': message,
                })
            else:
                message = Handover(user=user, msg=msg)
                message.save()
                return redirect('index')

        msg = Handover.objects.all().order_by('-date')
        paginator = Paginator(msg, 7)  # Show 7 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'recipe/handover.html', {
            # 'msg':msg,
            'page_obj': page_obj,
        })
    else:
        msg = 'Please Log in to Gain accses!'
        return render(request, 'recipe/base.html', {
            'msg': msg
        })


def delete_post(request, id):
    if request.user.is_staff:
        post = Handover.objects.filter(id=id)
        post.delete()

    return redirect('handover')

# delete recipe entry in eather(main recipe data or sub recipe data)


def delete(request, title):

    if request.user.is_staff:
        data = Recipe.objects.filter(title=title)
        subdata = Sub_recipe.objects.filter(title=title)
        data.delete()
        subdata.delete()

    return redirect('index')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    elif request.method == 'POST':
        form = registrationForm(request.POST or None)
        if form.is_valid():
            user = form.save()

            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=user.username, password=raw_password)
            # login user
            login(request, user)
            return redirect('index')
    else:
        form = registrationForm()
    return render(request, 'recipe/register.html', {'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
        # if not logged in then log in
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            # Check credential
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return render(request, 'recipe/login.html', {'error': "Your account has been desaibled."})

            else:
                return render(request, 'recipe/login.html', {'error': 'Invalid username or password. Try Again.'})

        return render(request, 'recipe/login.html')


def logout_user(request):
    if request.user.is_authenticated:

        logout(request)
        return redirect('login_user')
    else:
        return redirect('login_user')


def search(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            search_term = request.GET['q']
            result_recipe = Recipe.objects.filter(
                title__icontains=search_term).order_by('title')
            result_subrecipe = Sub_recipe.objects.filter(
                title__icontains=search_term).order_by('title')

            results = []
            for i in result_recipe:
                results.append(i.id)

            if not result_recipe:
                msg = 'There is NOT resipies with this key word!'

                return render(request, 'recipe/search.html', {
                    'message': msg
                })
            if not result_recipe:
                msg = 'There is NOT resipies with this key word!'

                return render(request, 'recipe/search.html', {
                    'message': msg
                })

            return render(request, 'recipe/search.html', {
                'out': result_recipe,
                'out_sub': result_subrecipe,
                'm': results,
            })
    else:
        msg = 'Please Log in to Gain accses!'
        return render(request, 'recipe/base.html', {
            'msg': msg
        })
