
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
pathFolder="pages/users/"

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    try:
        if request.method == "POST":
            username = request.POST['txtUserName']
            password = request.POST['txtPassword']
            user = authenticate(username=username,password=password,is_active='1')
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect("/")
                else:
                    messages.warning(request, "Username and Password is Invalid!")
                    render(request,pathFolder+"login.html")
    except Exception as ex:
        print("Error:" + str(ex))
    return render(request, pathFolder + "login.html")

def logout_view(request):
    logout(request)
    return redirect("/logins")
