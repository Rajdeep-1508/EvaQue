from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def homePage(request):
    data = {'page':"Home"}
    return render(request,"authentication/index.html",data)

def about(request):
    data = {'page':"About"}
    return render(request,"authentication/about.html",data)

def signin(request):
    data = {'page':"Login"}
    if request.method == "POST":
        username = request.POST['username']
        #emailid = request.POST['email']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"authentication/index.html",{'fname':fname})
        
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')


    return render(request,"authentication/login.html",data)

def signup(request):
    data = {'page':"SignUp"}
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        emailid = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,emailid,pass1)
        myuser.first_name = firstname

        myuser.save()

        messages.success(request,"Your account has been successfully Created")
        return redirect('login')

    return render(request,"authentication/signup.html",data)

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('home')  

def begForm(request):
    return render(request,"authentication/form.html")