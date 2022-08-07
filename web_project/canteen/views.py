from pyexpat.errors import messages
from django.shortcuts import render,redirect
from.models import Menus, Order
from django.contrib.auth.models import User,auth,AnonymousUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"registration/login.html")

def signup(request):
    form=UserCreationForm
    if request.method=='POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'User has been registered')
            return redirect('login')
    return render(request,"signup.html",{'form':form})

def logout(request):
    Session.objects.all().delete()
    return redirect("/")

def menu(request):
    menu=Menus.objects.all()
    print(menu)
    if request.method=='POST':
        return redirect('Products')
    return render(request, 'menu.html',context={'menu' : menu})