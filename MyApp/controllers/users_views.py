
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
pathFolder="pages/users/"

def login_view(request):
    if request.user.is_authenticated:
        return render(request,"")
    try:
        if request.method == "POST":
            username = request.POST['txtUserName']
            password = request.POST['txtPassword']
            user = authenticate(username=username,password=password)
            if user:
                if user:
                    login(request,user)
                    return render(request,"")
                else:
                    messages.warning(request, "Username and Password is Invalid!")
                    render(request,pathFolder+"login.html")
    except Exception as ex:
        print("Error:" + str(ex))
    return render(request, pathFolder + "login.html")
    # try:
    #     user=User()
    #     user.username=request.POST["txtUsername"]
    #     user.password = request.POST["txtPassword"]
    #     user1=authenticate(username=user.username,password=user.password)
    #     if user1:
    #         login(request,user)
    #         return redirect("/")
    #     else:
    #         messages.warning(request,"Username and Password is Invalid!")
    #         render(request,pathFolder+"login.html")
    # except Exception as ex:
    #     print("Error:" + str(ex))
    # return render(request,pathFolder+"login.html")

