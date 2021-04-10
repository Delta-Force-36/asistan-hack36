from django.urls import path,include
from .views import main,add_poll,vote,my_polls


urlpatterns = [
    path('',main,name='polling-main'),
    path('add_polling/',add_poll),
    path('<int:pollid>/vote/<int:p1>',vote),
    path('my_polls/',my_polls)
]