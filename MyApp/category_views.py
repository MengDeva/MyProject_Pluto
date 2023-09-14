from django.shortcuts import render
from MyApp.models import Category

# Create your views here.

def category(request):
    category=Category.objects.all()
    context={"categorys":category}
    return render(request, "pages/categorys/category.html",context)
