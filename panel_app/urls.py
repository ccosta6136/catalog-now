from django.urls import path

from panel_app.views import CatalogCreate, CatalogList, CatalogUpdate, PanelLogin, PanelLogout, ProductCreate, ProductDelete, ProductList, ProductUpdate, SignUpView, UserProfile, UserUpdate

urlpatterns = [
    path('', ProductList.as_view(), name='panel-page'),
    path('product/create', ProductCreate.as_view(), name ="product-create" ),
    path('product/<pk>/update', ProductUpdate.as_view(), name ="product-update" ),
    path('Product/<pk>/delete', ProductDelete.as_view(), name ="product-delete" ),
    path("login/", PanelLogin.as_view(), name="panel-login"),
    path("logout/", PanelLogout.as_view(), name="panel-logout"),
    path("signup/", SignUpView.as_view(), name="panel-signup"),
    path("user/<pk>", UserProfile.as_view(), name="user-detail"),
    path("user/<pk>/edit", UserUpdate.as_view(), name="user-update"),
    path('catalog/', CatalogList.as_view(), name='catalog-page'),
    path('catalog/create', CatalogCreate.as_view(), name ="catalog-create" ),
    path('catalog/<pk>/update', CatalogUpdate.as_view(), name ="catalog-update" ),
]