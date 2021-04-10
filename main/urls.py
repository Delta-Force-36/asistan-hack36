from django.urls import path,include


from .views import main,new_location,add_user_location,cpos


urlpatterns = [
    path('',main, name='main'),
    path('newlocation/',new_location),
    path('location/<int:pk>',add_user_location, name='main'),
    path('cpos/',cpos)
]