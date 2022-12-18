from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def homePage(request):
    data = {'page':"Home"}
    return render(request,"authentication/index.html",data)

def about(request):
    data = {'page':"About"}
    return render(request,"authentication/about.html",data)

def login(request):
    data = {'page':"Login"}
    return render(request,"authentication/login.html",data)


