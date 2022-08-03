from django.shortcuts import render

from catalog_now_app.models import Product
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class ProductList(ListView):
    queryset = Product.objects.all()
    #model = Product
    template_name = "catalog_now_app/product_list.html"
    context_object_name = "products"

class ProductDetail(DetailView):
    model = Product
    template_name = "catalog_now_app/product_detalle.html"

class ProductCreate(CreateView):
    model = Product
    success_url = reverse_lazy("panel-page")
    fields = ['product_title','short_description','description','price','image','author','is_headline','date_published']

class ProductUpdate(UpdateView):
    model = Product
    success_url = reverse_lazy("panel-page")
    fields = ['product_title','short_description','description','price','image','author','is_headline','date_published']

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy("panel-page")
