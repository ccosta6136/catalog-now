from django.contrib import admin
from catalog_now_app.models import Product, Publisher, Catalog

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Product)
admin.site.register(Catalog)