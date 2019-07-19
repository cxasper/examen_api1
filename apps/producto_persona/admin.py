# apps/producto_persona/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Producto_persona


# Register your models here.
@admin.register(Producto_persona)
class Producto_personaModelAdmin(admin.ModelAdmin):
    pass
