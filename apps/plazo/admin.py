# apps/plazo/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Plazo


# Register your models here.
@admin.register(Plazo)
class PlazoModelAdmin(admin.ModelAdmin):
    pass
