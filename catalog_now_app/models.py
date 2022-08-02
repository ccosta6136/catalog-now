from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Publisher(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"

class Product(models.Model):
    product_title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=180)
    description = RichTextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="articles", null=True, blank=True)
    author = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    is_headline= models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()

    def __str__(self):
        return f"{self.product_title}"


    
class Catalog(models.Model):
    name = models.CharField(max_length=20)
    social_network_one = models.URLField(null=True)
    social_network_two = models.URLField(null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
