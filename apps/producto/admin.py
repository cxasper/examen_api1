# apps/producto/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Producto


# Register your models here.
@admin.register(Producto)
class ProductoModelAdmin(admin.ModelAdmin):
    pass
