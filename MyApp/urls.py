from django.urls import path
from . import views, category_views

urlpatterns = [
    path("", views.dashboard),
    path("dashboard", views.dashboard, name="dashboard"),
    path("product", views.product),
    path("category",category_views.category),
    path("user", views.user),
]
