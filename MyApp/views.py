from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, "pages/dashboard.html")


def product(request):
    return render(request, "pages/product.html")


def user(request):
    return render(request, "pages/user.html")
