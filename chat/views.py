from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Person,Message


def logged_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/chat/')

    context = {}
    return render(request,'login.html',context)

def index(request):
    my_users = User.objects.all()
    return render(request,'chat/index.html',{'my_users':my_users})

@login_required(login_url="/chat/login/")
def room(request,user_name):
    my_users = User.objects.all()
    my_messages = Person.objects.get_or_new(request.user,user_name)
    return render(request,'chat/room.html',{
        'user_name':user_name,
        'my_users':my_users,
        'my_messages':my_messages
    })

