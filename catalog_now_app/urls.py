from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import home, AboutUs, MainPageView, ProductDetailView,ProductListUser





urlpatterns = [
    path('', home, name="index"),
    path('', MainPageView.as_view(), name='main-page'),
    path('about_us/', AboutUs.as_view(), name="about-us"),
    path('product/',  ProductListUser.as_view(), name ="product-list" ),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]

