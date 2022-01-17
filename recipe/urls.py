from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('input', views.input, name='input'),
    path('madara', views.madara, name='madara'),
    path('pizza', views.pizza, name='pizza'),
    path('amenities', views.amenities, name='amenities'),
    path('breakfast', views.breakfast, name='breakfast'),
    path('nest', views.nest, name='nest'),
    path('room', views.room_service, name='room_service'),
    path('recipe/<str:title>', views.recipe, name='recipe'),
    path('subrecipe/<int:id>/<str:title>', views.subrecipe, name='subrecipe'),
    path('handover', views.handover, name='handover'),
    path('delete/<str:title>', views.delete, name='delete'),
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),
    path('deletePost/<int:id>', views.delete_post, name='delete_post'),
    path('inputsub', views.inputsub, name='inputsub'),
    path('recipes', views.recipes, name='recipes'),
    path('search', views.search, name='search'),
    #path('archive', views.archived, name='archived')
]
