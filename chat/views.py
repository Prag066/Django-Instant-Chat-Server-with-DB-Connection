from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Person,Message


def RegisterUser(request):
    context = {}
    return render(request,'RegisterUser.html',context)

user_list = []
def logged_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            user_list.append(user.username)
            print('online',user_list)
            return redirect('/chat/')

    context = {}
    
    return render(request,'login.html',context)

def logged_out(request):
    user_list.remove(str(request.user.username))
    logout(request)
    return redirect('/chat/login/')

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

