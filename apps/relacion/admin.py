# apps/relacion/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Relacion


# Register your models here.
@admin.register(Relacion)
class RelacionModelAdmin(admin.ModelAdmin):
    pass
