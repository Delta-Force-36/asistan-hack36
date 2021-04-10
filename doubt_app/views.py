from django.shortcuts import render,redirect
from .models import doubts

def main(request):
    data={
        'doubts':doubts.objects.all(),
    }
    return render(request,'doubts/doubts.html',data)

def add_doubt(request):
    if request.method == 'POST' and request.user.is_authenticated:
        p1 = request.POST.get('p1')
        p2 = request.POST.get('p2')
        p3 = request.POST.get('p3')

        
        poll = polls.objects.create(name = p1 , topic = p2 , doubt = p3 ,auth = request.user)
        return redirect('/doubts')
        
    return render(request,'polling/add_doubts.html')
