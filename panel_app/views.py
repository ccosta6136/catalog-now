from django.shortcuts import render

from catalog_now_app.models import Product, Publisher, Catalog
from catalog_now_app.views import BaseView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
class ProductList(LoginRequiredMixin,BaseView, ListView):
    queryset = Product.objects.all()
    #model = Product
    template_name = "catalog_now_app/product_list.html"
    context_object_name = "products"

class ProductDetail(LoginRequiredMixin, BaseView, DetailView):
    model = Product 
    template_name = "catalog_now_app/product_detalle.html"

class ProductCreate(LoginRequiredMixin, BaseView, CreateView):
    model = Product
    success_url = reverse_lazy("panel-page")
    fields = ['product_title','short_description','description','price','image','author','is_headline','date_published']
    permission_required = ("catalog_now_app.add_product")

class ProductUpdate(LoginRequiredMixin, BaseView, UpdateView):
    model = Product
    success_url = reverse_lazy("panel-page")
    fields = ['product_title','short_description','description','price','image','author','is_headline','date_published']
    permission_required = ("catalog_now_app.change_product")

class ProductDelete(LoginRequiredMixin, BaseView, DeleteView):
    model = Product
    success_url = reverse_lazy("panel-page")
    permission_required = ("catalog_now_app.delete_product")

class PanelLogin(LoginView, BaseView):
    template_name = 'catalog_now_app/panel_login.html'
    next_page = reverse_lazy("panel-page")

class PanelLogout(LogoutView, BaseView):
    template_name = 'catalog_now_app/panel_logout.html'
    #next_page = reverse_lazy("panel-login")

class SignUpView(SuccessMessageMixin, BaseView, CreateView):
    template_name = 'catalog_now_app/panel_create_account_form.html'
    success_url = reverse_lazy('panel-page')
    form_class = UserCreationForm
    success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

class UserProfile(LoginRequiredMixin, UserPassesTestMixin,  BaseView, DetailView):
    model = User
    template_name = "user_profile/user_detail.html"

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, BaseView, UpdateView):
    model = User
    template_name = "user_profile/user_form.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
        return reverse_lazy("user-detail", kwargs={"pk": self.request.user.id})

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

class CatalogList(LoginRequiredMixin, BaseView, ListView):
    queryset = Catalog.objects.all()
    template_name = "catalog_now_app/catalog_list.html"
    context_object_name = "catalogs"

class CatalogCreate(LoginRequiredMixin, BaseView, CreateView):
    model = Catalog
    success_url = reverse_lazy("catalog-page")
    fields = ['name','social_network_one','social_network_two','email']

class CatalogUpdate(LoginRequiredMixin, BaseView, UpdateView):
    model = Catalog
    success_url = reverse_lazy("catalog-page")
    fields = ['name','social_network_one','social_network_two','email']