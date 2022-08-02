from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import home, SobreNosotros, MainPageView, ProductDetailView




urlpatterns = [
    path('', home, name="index"),
    path('', MainPageView.as_view(), name='main-page'),
    path('sobre_nosotros/', SobreNosotros.as_view(), name="sobre-nosotros"),
    path('product/<pk>/', ProductDetailView.as_view(), name='product-detail'),
]

