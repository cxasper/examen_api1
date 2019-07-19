# apps/persona/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Persona


# Register your models here.
@admin.register(Persona)
class PersonaModelAdmin(admin.ModelAdmin):
    pass
