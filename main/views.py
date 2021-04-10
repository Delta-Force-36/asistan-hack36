from django.shortcuts import render

# Create your views here.
def main(request):

    user = request.user 

    data = {
        'user':user,
    }
    return render(request,'main/base.html',data)