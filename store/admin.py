from django.contrib import admin

# Register your models here.
from .models import Product, Command

admin.site.register(Product)
admin.site.register(Command)