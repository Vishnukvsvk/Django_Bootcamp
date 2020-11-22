"""bootcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from producti import views

urlpatterns = [
    path('badview/', views.bad_view),
    path('products/create/', views.form_view),
    path('products/<int:id>/', views.Product_Dynamic_View),
    path('snippy/', views.product_snippet_view),
    path('product/1/', views.Product_View),
    path('home/', views.Home_View),
    path('admin/', admin.site.urls),
]
