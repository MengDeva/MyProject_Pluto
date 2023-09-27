import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST

from MyApp.models.models import Product, Category

# Create your views here.
pathFolder = "pages/products/"


def index(request):
    if 'search' in request.GET:
        search = request.GET['search']
        product = Product.objects.filter(name__icontains=search)
    else:
        product = Product.objects.all()
    context = {'products': product}
    return render(request, pathFolder + "index.html", context)


def create(request):
    category = Category.objects.all()
    context = {"categorys": category}
    return render(request, pathFolder + "add_product.html", context)

@require_POST
def store(request):
    try:
        product = Product()
        product.name = request.POST["txtName"]
        product.barcode = request.POST["txtBarcode"]
        product.unitPrice = request.POST["txtUnitPrice"]
        product.qtyInstock = request.POST["txtQty"]
        product.photo = request.FILES['file']
        product.category_id = request.POST["ddlCategoryID"]
        product.createBy = 1
        messages.success(request, "product Created")
        product.save()
    except Exception as ex:
        print("Error:" + str(ex))
    return redirect("/product/create")


def destroy(request, id):
    try:
        product = Product.objects.get(pk=id)
        product.delete()
    except Exception as ex:
        print("Error:" + str(ex))
    return redirect("/product")


def edit(request, id):
    try:
        product = Product.objects.get(pk=id)
        context = {"product": product}
    except Exception as ex:
        print("Error:" + str(ex))
    return render(request, pathFolder + "edit.html", context)


def update(request):
    try:
        product = Product()
        product.id = request.POST["txtId"]
        product.name = request.POST["txtName"]
        c1 = product.objects.get(pk=product.id)
        if c1:
            c1.name = product.name;
            c1.updateAt = datetime.datetime.now()
            c1.updateBy = 1;
            c1.save()
            messages.success(request, "product Updated")
    except Exception as ex:
        print("Error:" + str(ex))
    return redirect("/product/edit/" + product.id)
