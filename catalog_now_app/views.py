from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
from catalog_now_app.models import Product, Catalog
# Create your views here.

class BaseView(View):
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headline'] = Product.objects.filter(is_headline=True).order_by('date_updated').first()
        context['catalog'] = Catalog.objects.order_by('date_updated').first()
        return context

class MainPageView(TemplateView):
    template_name = "catalog_now_app/index.html" 

class SobreNosotros(BaseView, TemplateView):
    template_name = "catalog_now_app/sobre_nosotros.html"        

class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalog'] = Catalog.objects.order_by('date_updated').first()
        return context