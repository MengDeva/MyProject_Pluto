from datetime import datetime
import os
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from MyApp.models.models import Product, Category

# Create your views here.
pathFolder = "pages/products/"


@require_GET
def index(request):
    if 'search' in request.GET:
        search = request.GET['search']
        product = Product.objects.filter(name__icontains=search)
    else:
        product = Product.objects.all()
    context = {'products': product}
    return render(request, pathFolder + "index.html", context)

@require_GET
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
        p1=Product.objects.filter(name=product.name)
        if p1:
            messages.success(request,"Product Name has been already Used")
            return redirect("/product/create")
        p2 = Product.objects.filter(name=product.barcode)
        if p2:
            messages.success(request,"Barcode has been Used")
            return redirect("/product/create")
        product.unitPrice = request.POST["txtUnitPrice"]
        product.qtyInstock = request.POST["txtQty"]
        # product.photo = request.FILES['file']
        product.category_id = request.POST["ddlCategoryID"]
        product.createBy = 1
        if len(request.FILES)>0:
            product.photo = request.FILES['file']
            product.save()
            messages.success(request, "Product Created")
        else:
            product.photo = ""
            product.save()
            messages.success(request, "Product Created")
    except Exception as ex:
        print("Error:" + str(ex))
    return redirect("/product/create")
@require_GET
def destroy(request, id):
    try:
        product = Product.objects.get(pk=id)
        if product.photo:
            product.photo.delete()
            product.delete()
        else:
            product.delete()
    except Exception as ex:
        print("Error:" + str(ex))
    return redirect("/product")

@require_GET
def edit(request, id):
    try:
        product = Product.objects.get(pk=id)
        category = Category.objects.all()
        context = {"product": product,"categorys": category}
    except Exception as ex:
        print("Error:" + str(ex))
    return render(request, pathFolder + "edit.html", context)

@require_POST
def update(request):
    try:
        product = Product()
        product.id=request.POST["txtId"]
        product.name = request.POST["txtName"]
        product.barcode = request.POST["txtBarcode"]
        product.unitPrice = request.POST["txtUnitPrice"]
        product.qtyInstock = request.POST["txtQty"]
        product.category_id = request.POST["ddlCategoryID"]
        product.updateBy = 2
        product.updateAt=datetime.now()
        p1=Product.objects.get(pk=product.id)
        if p1:
            if p1.photo:
                p1.name=product.name
                p1.barcode=product.barcode
                p1.unitPrice=product.unitPrice
                p1.qtyInstock=product.qtyInstock
                p1.category_id=product.category_id
                p1.updateBy=product.updateBy
                p1.updateAt=product.updateAt
                if len(request.FILES)>0:
                    p1.photo.delete()
                    p1.photo = request.FILES["file"]
                    p1.save()
                    messages.success(request, "Product Updated")
                else:
                    p1.save()
                    messages.success(request, "Product Updated")
            else:
                p1.name = product.name
                p1.barcode = product.barcode
                p1.unitPrice = product.unitPrice
                p1.qtyInstock = product.qtyInstock
                p1.category_id = product.category_id
                p1.updateBy = product.updateBy
                p1.updateAt = product.updateAt
                if len(request.FILES) > 0:
                    if len(product.photo) > 0:
                        os.remove(product.photo.path)
                    product.photo = request.FILES['file']
                    p1.save()
                    messages.success(request, "Product Updated")
                else:
                    p1.save()
                    messages.success(request, "Product Updated")
    except Exception as ex:
        print("Error:" + str(ex))
    return redirect("/product")
@require_GET
def view(request,id):
    try:
        product = Product.objects.select_related("category").get(pk=id)
        category = Category.objects.all()
        context = {"product": product,"categorys": category}
    except Exception as ex:
        print("Error:"+str(ex))
    return render(request,pathFolder + "view.html", context)
