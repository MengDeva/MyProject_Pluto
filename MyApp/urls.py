from django.urls import path
from . import views, user_views
from .controllers import category_views,product_views

urlpatterns = [
    path("", views.dashboard),
    path("dashboard", views.dashboard, name="dashboard"),
path("user", user_views.index),
    path("users", views.user),
    #------Category------#
    path("category", category_views.index),
    path("category/create", category_views.create),
    path("category/store", category_views.store),
    path("category/destroy/<id>", category_views.destroy),
    path("category/edit/<id>", category_views.edit),
    path("category/update", category_views.update),
    #------Product------#
    path("product", product_views.index),
    path("product/create", product_views.create),
    path("product/store", product_views.store),
    path("product/destroy/<id>", product_views.destroy),
    path("product/edit/<id>", product_views.edit),
    path("product/update", product_views.update),
]
