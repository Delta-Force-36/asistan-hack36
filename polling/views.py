from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .models import polls, my_vote

def main(request):
    data = {
        'polls':polls.objects.all(),
    }

    return render(request,'polling/polling.html',data)

def add_poll(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            p1 = request.POST.get('p1')
            p2 = request.POST.get('p2')
            p3 = request.POST.get('p3')
            p4 = request.POST.get('p4')

            p1_url = request.POST.get('p1_url')
            p2_url = request.POST.get('p2_url')
            p3_url = request.POST.get('p3_url')
            p4_url = request.POST.get('p4_url')
            
            poll = polls.objects.create(name1 = p1 , name2 = p2 , name3 = p3 , name4 = p4 , img1 = p1_url , img2 = p2_url , img3 = p3_url , img4 = p4_url , auth = request.user)
            return redirect('/polling')
        else:
            return render(request,'polling/add_poll.html')
    else:
        messages.warning(request, 'Login / Sign Up to add your polls')
        return render(request,'polling/add_poll.html')
    return render(request,'polling/add_poll.html')


def vote(request,pollid,p1):
    if request.user.is_authenticated:
        poll = polls.objects.all().filter(id=pollid)[0]


        check = my_vote.objects.all().filter(votes = poll)

        data = {
            'polls':polls.objects.all(),
        }
        if len(check) == 0:
            check = my_vote(auth=request.user,votes=poll)
            check.save()
            if p1 == 1:
                poll.vote1 = poll.vote1 +1
                poll.save()

            if p1 == 2:
                poll.vote2 = poll.vote2 +1
                poll.save()

            if p1 == 3:
                poll.vote2 = poll.vote3 +1
                poll.save()

            if p1 == 4:
                poll.vote2 = poll.vote4 +1
                poll.save()
            return render(request,'polling/polling.html',data)
        else:
            messages.warning(request, 'Already Voted') 
            return render(request,'polling/polling.html',data)
    else:
        messages.warning(request, 'Login / Sign Up to add your polls') 
        return render(request,'polling/polling.html')


def my_polls(request):
    if request.user.is_authenticated:
        poll = polls.objects.all().filter(auth = request.user)
        data = {
            'polls':polls.objects.all(),
            'my_poll':True
        }
        return render(request,'polling/polling.html',data)
    else:
        messages.warning(request, 'Login / Sign Up to check your Polls')
        return render(request,'polling/polling.html')


