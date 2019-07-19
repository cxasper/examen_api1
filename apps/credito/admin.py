# apps/credito/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Credito


# Register your models here.
@admin.register(Credito)
class CreditoModelAdmin(admin.ModelAdmin):
    pass
