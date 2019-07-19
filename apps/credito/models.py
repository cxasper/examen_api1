# apps/credito/models.py
# Python imports


# Django imports
from django.db import models

# Third party apps imports


# Local imports


# Create your models here.
class Credito(models.Model):
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)
