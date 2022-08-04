from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Product, Catalog

# Create your views here.

def home(request):
    return render(request, 'catalog_now_app/index.html')

class BaseView(View):
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headline'] = Product.objects.filter(is_headline=True).order_by('date_updated').first()
        context['catalog'] = Catalog.objects.order_by('date_updated').first()
        return context    

class AboutUs(BaseView, TemplateView):
    template_name = "catalog_now_app/about_us.html"        

class MainPageView(BaseView):
    template_name = "catalog_now_app/index.html"   

class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog_now_app/product_detail.html"  
   

class ProductListUser(ListView):
    model = Product
    template_name = "catalog_now_app/list_products.html"
    context_object_name = "products"
  
     