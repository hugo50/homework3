from django.shortcuts import render
from django.template import RequestContext
from User.forms import *
from User.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    context = {'where_am_i':'In index'}
    return render(request,'User/index.html',context)

def analyze_url(request,user):
    up = UserProfile.objects.get(user=user)
    if up.secret:
        return
    state = up.knock_position
    url = request.path
    current_state = ''
    next_state = ''
    print state
    if state == 0:
        print 'Here0'
        current_state = up.knock_url_0
    elif state == 1:
        print 'Here1'
        current_state = up.knock_url_1
    elif state == 2:
        print 'Here2'
        current_state = up.knock_url_2
    elif state == 3:
        print 'Here3'
        current_state = up.knock_url_3
    print current_state
    print url 
    if current_state == url:
        if state == 3:
            up.secret = True
            print 'SUCCESSS'        
        else: 
            up.knock_position += 1
    up.save()
    return

def register(request):
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user)
        analyze_url(request,user)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            uname = request.POST['username']
            pwd = request.POST['password1']
            user = User.objects.create_user(uname,'',pwd)
            if user is None:
                return HttpResponse('create user failed')
            up = UserProfile(user=user)
            up.getHash()
            up.save()
            return HttpResponseRedirect('/user/login/')
    else:
        form = RegisterForm

    return render(request, 'User/register.html',{'form':form})

def my_login(request):
    error = ''
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user)
        analyze_url(request,user)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = request.POST['username']
            pwd = request.POST['password']
            user = authenticate(username=user_name,password=pwd)
            
            if user is not None:
                if user.is_active:
                    up = UserProfile(user=user)
                    up.getHash()
                    login(request,user)
                    return HttpResponseRedirect('/message/add/')
            else:
                error = 'Login Failed. Try Again'
        else:
            error = 'Form not valid. Try Again'
        return render(request, 'User/login.html',{'form':form,'error':error})
    else:
        form = LoginForm
    return render(request, 'User/login.html',{'form':form,'error':error})


@login_required(login_url='/user/login/')
def my_logout(request):
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user)
        up = UserProfile.objects.get(user=user)
        up.secret = False 
        up.save()
    logout(request)
    return render(request, 'User/logout.html',)

@login_required(login_url='/user/login/')
def add(request):
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user)
        analyze_url(request,user)
        up = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        form = MessageAddForm(request.POST)
        title = request.POST['title']
        body = request.POST['message']
        if up.secret:
            m = Secret_Message(title=title,message=body,owner=user)
            m.save()
        else:
            m = Message(title=title,message=body,owner=user)
            m.save()
        return render(request, 'User/message_add.html',{'form':form})
    else:
        form = MessageAddForm   
    return render(request, 'User/message_add.html',{'form':form})

@login_required(login_url='/user/login/')
def list_msg(request):
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user)
        analyze_url(request,user)
        up = UserProfile.objects.get(user=user)
    if up.secret:
        secret = 'secret'
        msg_set = Secret_Message.objects.all()
    else:
        secret = 'not secret'
        msg_set = Message.objects.all()
    return render(request, 'User/message_list.html',{'message':msg_set,'state':secret})


def msg_index(request):
    return HttpResponse('In msg_index')

