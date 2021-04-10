from django.shortcuts import render
from django.contrib.auth.models import User
from .models import location
# Create your views here.
def main(request):

    user = request.user 

    data = {
        'user':user,
    }
    return render(request,'main/base.html',data)

def new_location(request):
    if request.method == "POST":
        ln = request.POST.get('location_name')
        loc = location(location_name = ln,auth=request.user)
        loc.save()
        loc.save()
    # l = location(location_name = 'place2',auth=request.user)
    # l.save()
    # l.save()
    return render(request,'main/add_location.html')