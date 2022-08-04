from django.shortcuts import render

from catalog_now_app.models import Product, Publisher
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
class ProductList(LoginRequiredMixin, ListView):
    queryset = Product.objects.all()
    #model = Product
    template_name = "catalog_now_app/product_list.html"
    context_object_name = "products"

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog_now_app/product_detalle.html"

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    success_url = reverse_lazy("panel-page")
    fields = ['product_title','short_description','description','price','image','author','is_headline','date_published']

class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy("panel-page")
    fields = ['product_title','short_description','description','price','image','author','is_headline','date_published']

class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("panel-page")

class PanelLogin(LoginView):
    template_name = 'catalog_now_app/panel_login.html'
    next_page = reverse_lazy("panel-page")

class PanelLogout(LogoutView):
    template_name = 'catalog_now_app/panel_logout.html'

class SignUpView(SuccessMessageMixin, UserPassesTestMixin, CreateView):
    template_name = 'catalog_now_app/panel_create_account_form.html'
    success_url = reverse_lazy('panel-page')
    form_class = UserCreationForm
    success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

class UserProfile(LoginRequiredMixin, DetailView):
    model = Publisher
    template_name = "user_profile/user_detail.html"

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = "user_profile/user_form.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
        return reverse_lazy("user-detail", kwargs={"pk": self.request.user.id})

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])