from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url="/logins")
# Create your views here.
def dashboard(request):
    return render(request, "pages/dashboard.html")

def product(request):
    return render(request, "pages/product.html")


def user(request):
    return render(request, "pages/users.html")
