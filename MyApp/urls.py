from django.urls import path
from . import views, user_views
from .controllers import category_views,product_views
from .controllers import users_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.dashboard),
    path("dashboard", views.dashboard, name="dashboard"),
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
    path("product/view/<id>", product_views.view),
    path("logins",users_views.login_view),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
