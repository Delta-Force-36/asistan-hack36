from django.contrib import admin
from .models import location,user_locations

admin.site.register(location)
admin.site.register(user_locations)

# Register your models here.
