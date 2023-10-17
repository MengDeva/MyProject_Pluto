import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET



# Create your views here.
pathFolder="pages/users/"
def login_view(request):
    try:
        user=User()
        user.username=request.POST["txtUsername"]
        user.password = request.POST["txtPassword"]
        user1=authenticate(username=user.username,password=user.password,is_active="t")
        if user1:
            login(request,user1)
            return redirect("/")
        else:
            messages.warning(request,"Username and Password is Invalid!")
            render(request,pathFolder+"login.html")
    except Exception as ex:
        print("Error:" + str(ex))
    return render(request,pathFolder+"login.html")

