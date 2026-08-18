from django.contrib import admin
from django.urls import path
from . import views
from . import catalog_views   # <-- your new file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('search/', views.search),
    path('report/', views.report),
    path('catalog/', catalog_views.catalog),   # <-- FIXED
]
