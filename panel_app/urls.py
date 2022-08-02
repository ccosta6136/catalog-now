from django.urls import path

from panel_app.views import ProductCreate, ProductDelete, ProductList, ProductUpdate

urlpatterns = [
    path('', ProductList.as_view(), name='panel-page'),
    path('product/create', ProductCreate.as_view(), name ="product-create" ),
    path('product/<pk>/update', ProductUpdate.as_view(), name ="product-update" ),
    path('Product/<pk>/delete', ProductDelete.as_view(), name ="product-delete" ),
]