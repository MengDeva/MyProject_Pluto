from django.urls import path
from . import views, category_views, user_views

urlpatterns = [
    path("", views.dashboard),
    path("dashboard", views.dashboard, name="dashboard"),
    path("product", views.product),
    path("users", views.user),
    path("category", category_views.index),
    path("category/create", category_views.create),
    path("category/store", category_views.store),
    path("category/destroy/<id>", category_views.destroy),
    path("category/edit/<id>", category_views.edit),
    path("category/update", category_views.update),
    path("user", user_views.index),
]
