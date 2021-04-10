from django.shortcuts import render
from django.contrib.auth.models import User
from .models import location,user_locations
from django.contrib import messages
# Create your views here.
def main(request):

    user = request.user 

    data = {
        'user':user,
    }
    return render(request,'main/base.html',data)

def new_location(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            ln = request.POST.get('location_name')
            loc = location(location_name = ln,auth=request.user)
            loc.save()
            loc.save()
            return render(request,'main/add_location.html')
        return render(request,'main/add_location.html')

    else:
        messages.warning(request, 'Login / Sign Up to add locations')
        return render(request,'main/add_location.html')

def add_user_location(request,pk):
    if request.user.is_authenticated:
        loc = location.objects.all().filter(id = pk)[0]
        user_loc = user_locations(auth = request.user,locations = loc)
        user_loc.save()

        inf_loc = user_locations.objects.all().filter(locations = loc)
        for loc in inf_loc:
            print(loc.locations.location_name)
        data = {
            'msg':"Your Location has been added"
        }
        return render(request,'main/add_user_location.html',data)
    else:
        messages.warning(request, 'Login / Sign Up to add your location')
        return render(request,'main/add_location.html')

def cpos(request):
    if request.user.is_authenticated:
        inf = user_locations.objects.all().filter(auth = request.user)
        for i in inf:
            i.infected = True
            i.save()
        return render(request,'main/cpos.html')
    else:
        messages.warning(request, 'Login / Sign Up')
        return render(request,'main/cpos.html')
