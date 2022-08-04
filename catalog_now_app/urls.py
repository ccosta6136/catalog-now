"""catalog_now URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
<<<<<<< HEAD
from catalog_now_app.views import SobreNosotros, MainPageView, ProductDetailView
=======
from .views import home, AboutUs, MainPageView, ProductDetailView,ProductListUser




>>>>>>> origin/main

urlpatterns = [
    #path('', home, name="index"),
    path('', MainPageView.as_view(), name='main-page'),
<<<<<<< HEAD
    path('sobre_nosotros/', SobreNosotros.as_view(), name="sobre-nosotros"),
    path('product/<pk>/', ProductDetailView.as_view(), name='product-detail'),
]
=======
    path('about_us/', AboutUs.as_view(), name="about-us"),
    path('product/',  ProductListUser.as_view(), name ="product-list" ),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]

>>>>>>> origin/main
