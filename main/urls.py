from django.urls import path,include


from .views import main,new_location


urlpatterns = [
    path('',main, name='main'),
    path('newlocation/',new_location, name='main'),
    path('newlocation/',new_location, name='main'),
]