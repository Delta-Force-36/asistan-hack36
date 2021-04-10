from django.contrib import admin
from .models import polls,my_vote
# Register your models here.
admin.site.register(polls)
admin.site.register(my_vote)