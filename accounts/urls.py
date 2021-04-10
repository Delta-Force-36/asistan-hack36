
from django.urls import path
from .views import regis,login,logout

urlpatterns = [
    path('login/',login,name='profile-login'),
    path('regis/',regis,name='profile-regis'),
    path('logout/',logout,name='profile-logout')

]