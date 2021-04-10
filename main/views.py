from django.shortcuts import render
from django.contrib.auth.models import User
from .models import location,user_locations
from django.contrib import messages
# Create your views here.
def main(request):
    if request.user.is_authenticated:
        data = {
            'locs':location.objects.all().filter(auth = request.user)
        }
        print(data)
        return render(request,'main/locations.html',data)
    return render(request,'main/base.html')

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

        if loc.infected:
            messages.warning(request, 'Your Location Has been infected')
            return render(request,'main/add_user_location.html')
        else:
            data = {
                'msg':"Your Location has been added and This place is not infected"
            }
            return render(request,'main/add_user_location.html',data)
    else:
        messages.warning(request, 'Login / Sign Up to add your location')
        return render(request,'main/add_user_location.html')

def cpos(request):
    if request.user.is_authenticated:
        inf = user_locations.objects.all().filter(auth = request.user)
        for i in inf:
            i.locations.infected = True
            i.locations.save()
            i.infected = True
            i.save()
        return render(request,'main/cpos.html')
    else:
        messages.warning(request, 'Login / Sign Up')
        return render(request,'main/cpos.html')
