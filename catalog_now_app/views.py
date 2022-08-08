from asyncio.windows_events import NULL
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
from catalog_now_app.models import Product, Catalog, Publisher
# Create your views here.

class BaseView(View):
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalog'] = Catalog.objects.order_by('-date_updated').first()
        if self.request.user.is_authenticated:
            context['publisher'] = Publisher.objects.get(user_id=self.request.user.id)
        return context

class MainPageView(BaseView, TemplateView):
    template_name = "catalog_now_app/index.html" 

class AboutUs(BaseView, TemplateView):
    template_name = "catalog_now_app/about_us.html"        

class ProductDetailView(BaseView, DetailView):
    model = Product
    template_name = "catalog_now_app/product_detail.html"  
   
class ProductListUser(BaseView,ListView):
    model = Product
    template_name = "catalog_now_app/list_products.html"
    context_object_name = "products"
  
     