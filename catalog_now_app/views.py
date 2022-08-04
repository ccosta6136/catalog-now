from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
<<<<<<< HEAD
from catalog_now_app.models import Product, Catalog
=======
from .models import Product, Catalog

>>>>>>> origin/main
# Create your views here.

class BaseView(View):
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headline'] = Product.objects.filter(is_headline=True).order_by('date_updated').first()
        context['catalog'] = Catalog.objects.order_by('date_updated').first()
        return context

class MainPageView(TemplateView):
    template_name = "catalog_now_app/index.html" 

class AboutUs(BaseView, TemplateView):
    template_name = "catalog_now_app/about_us.html"        

class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog_now_app/product_detail.html"  
   

class ProductListUser(ListView):
    model = Product
    template_name = "catalog_now_app/list_products.html"
    context_object_name = "products"
  
     