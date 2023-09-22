import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET

from MyApp.models.models import Category


# Create your views here.
pathFolder="pages/categorys/"
def index(request):
    if 'search' in request.GET:
        search = request.GET['search']
        category = Category.objects.filter(name__icontains=search)
    else:
        category = Category.objects.all()
    context = {'categorys': category}
    return render(request,pathFolder + "index.html", context)


def create(request):

    return render(request, pathFolder + "add_product.html")


def store(request):
    try:
        category = Category()
        category.name = request.POST["txtName"]
        category.createBy = 1
        messages.success(request, "Category Created")
        category.save()
    except Exception as ex:
        print("Error:" + str(ex))
    return redirect("/category/create")



def destroy(request, id):
    try:
        category = Category.objects.get(pk=id)
        category.delete()
    except Exception as ex:
        print("Error:" + str(ex))
    return redirect("/category")


def edit(request, id):
    try:
        category = Category.objects.get(pk=id)
        context = {"category": category}
    except Exception as ex:
        print("Error:" + str(ex))
    return render(request, pathFolder + "edit.html", context)


def update(request):
    try:
        category = Category()
        category.id = request.POST["txtId"]
        category.name = request.POST["txtName"]
        c1 = Category.objects.get(pk=category.id)
        if c1:
            c1.name = category.name;
            c1.updateAt = datetime.datetime.now()
            c1.updateBy = 1;
            c1.save()
            messages.success(request,"Category Updated")
    except Exception as ex:
        print("Error:" + str(ex))
    return redirect("/category/edit/" + category.id)
