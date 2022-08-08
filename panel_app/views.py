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

from django import forms


# Create your views here.
class ProductList(LoginRequiredMixin, BaseView, ListView):
    queryset = Product.objects.all()
    template_name = "catalog_now_app/product_list.html"
    context_object_name = "products"


class AdminProducts(LoginRequiredMixin, SuccessMessageMixin,  BaseView, ListView):
    queryset = Product.objects.all()
    template_name = "catalog_now_app/admin_products.html"
    context_object_name = "products"

class ProductDetail(LoginRequiredMixin, BaseView, DetailView):
    model = Product 
    template_name = "catalog_now_app/product_detalle.html"


class ProductCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, BaseView, CreateView):
    model = Product
    success_url = reverse_lazy("panel-page")
    fields = ['product_title','short_description','description','price','image','author']
    permission_required = ("catalog_now_app.add_product")
    success_message = "¡¡ Producto creado !!"


class ProductUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, BaseView, UpdateView):
    model = Product
    success_url = reverse_lazy("panel-page")
    fields = ['product_title','short_description','description','price','image','author']
    permission_required = ("catalog_now_app.change_product")
    success_message = "¡¡ Producto actualizado !!"


class ProductDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, BaseView, DeleteView):
    model = Product
    success_url = reverse_lazy("panel-page")
    permission_required = ("catalog_now_app.delete_product")
    success_message = "¡¡ Producto eliminado !!"


class PanelLogin(SuccessMessageMixin, BaseView, LoginView):
    template_name = 'catalog_now_app/panel_login.html'
    next_page = reverse_lazy("product-admin")
    success_message = "¡¡ Bienvenido %(username)s!!"


class PanelLogout(SuccessMessageMixin, BaseView, LogoutView):
    next_page = reverse_lazy("panel-login")
    success_message = "¡¡ Adios %(username)s!!"
    

class SignUpView(SuccessMessageMixin, BaseView, CreateView):
    template_name = 'catalog_now_app/panel_create_account_form.html'
    success_url = reverse_lazy('product-admin')
    form_class = UserCreationForm
    success_message = "¡¡ Cuenta creada satisfactoriamente !!"
    

class UserProfile(LoginRequiredMixin, UserPassesTestMixin,  BaseView, DetailView):
    model = User
    template_name = "user_profile/user_detail.html"

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, BaseView, UpdateView):
    model = User
    template_name = "user_profile/user_form.html"
    fields = ["username", "email", "first_name", "last_name"]
    success_message = "¡¡ Perfil actualizado !!"

    def get_success_url(self):
        return reverse_lazy("user-detail", kwargs={"pk": self.request.user.id})

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])


class PublisherUpdate(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, BaseView, UpdateView):
    model = Publisher
    template_name = "user_profile/publisher_form.html"
    fields = ["avatar"]
    success_message = "¡¡ Avatar actualizado !!"

    def get_success_url(self):
        return reverse_lazy("user-detail", kwargs={"pk": self.request.user.id})

    def test_func(self):
        consulta = Publisher.objects.get(id=self.kwargs['pk'])
        return self.request.user.id == int(consulta.user_id)


class CatalogList(LoginRequiredMixin, BaseView, ListView):
    queryset = Catalog.objects.all()
    template_name = "catalog_now_app/catalog_list.html"
    context_object_name = "catalogs"


class CatalogCreate(LoginRequiredMixin, SuccessMessageMixin, BaseView, CreateView):
    model = Catalog
    success_url = reverse_lazy("catalog-page")
    fields = ['name','social_network_twitter','social_network_instagram', 'social_network_linkedin','email', 'address', 'city', 'zip_code', 'country', 'phone', 'whatsapp_phone_number']
    success_message = "¡¡ Catalogo creado !!"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(CatalogCreate, self).get_form(form_class)
        form.fields['social_network_twitter'].required = False
        form.fields['social_network_instagram'].required = False
        form.fields['social_network_linkedin'].required = False
        form.fields['phone'].widget = forms.TextInput(attrs={'placeholder': '+54 9 11 2345-6789'})
        form.fields['whatsapp_phone_number'].required = False
        form.fields['whatsapp_phone_number'].widget = forms.TextInput(attrs={'placeholder': '5491123456789'})
        return form


class CatalogUpdate(LoginRequiredMixin, SuccessMessageMixin, BaseView, UpdateView):
    model = Catalog
    success_url = reverse_lazy("catalog-page")
    fields = ['name','social_network_twitter','social_network_instagram', 'social_network_linkedin','email', 'address', 'city', 'zip_code', 'country', 'phone', 'whatsapp_phone_number']
    success_message = "¡¡ Catalogo actualizado !!"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(CatalogUpdate, self).get_form(form_class)
        form.fields['social_network_twitter'].required = False
        form.fields['social_network_instagram'].required = False
        form.fields['social_network_linkedin'].required = False
        form.fields['phone'].widget = forms.TextInput(attrs={'placeholder': '+54 9 11 2345-6789'})
        form.fields['whatsapp_phone_number'].required = False
        form.fields['whatsapp_phone_number'].widget = forms.TextInput(attrs={'placeholder': '5491123456789'})
        return form