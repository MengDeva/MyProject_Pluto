from django.core.checks import messages
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    # user = User.objects.all()
    # context = {"peoples": user}
    return render(request, "pages/users/index.html")

# def create(request):
#     return render(request, "pages/categorys/add_category.html")
#
#
# def store(request):
#     try:
#         category = Category()
#         category.name = request.POST["txtName"]
#         category.createBy = 1
#         category.save()
#         messages.success(request, "Category Created")
#     except Exception as ex:
#         print("Error:" + str(ex))
#     return redirect("/category/create")
#
#
# def destroy(request, id):
#     try:
#         category = Category.objects.get(pk=id)
#         category.delete()
#     except Exception as ex:
#         print("Error:" + str(ex))
#     return redirect("/category")
#
#
# def edit(request, id):
#     try:
#         category = Category.objects.get(pk=id)
#         context = {"category": category}
#     except Exception as ex:
#         print("Error:" + str(ex))
#     return render(request, "pages/categorys/edit.html", context)
#
#
# def update(request):
#     try:
#         category = Category()
#         category.id = request.POST["txtId"]
#         category.name = request.POST["txtName"]
#         c1 = Category.objects.get(pk=category.id)
#         if c1:
#             c1.name = category.name;
#             c1.save()
#     except Exception as ex:
#         print("Error:" + str(ex))
#     return redirect("/category/edit/" + category.id)
