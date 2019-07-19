# apps/producto_persona/models.py
# Python imports


# Django imports
from django.db import models

# Third party apps imports


# Local imports
from apps.persona.models import Persona
from apps.producto.models import Producto
from apps.relacion.models import Relacion
# Create your models here.
class Producto_persona(models.Model):
    producto_id = models.ForeignKey(
        Producto,
        on_delete=models.DO_NOTHING
    )
    persona_id = models.ForeignKey(
        Persona,
        on_delete=models.DO_NOTHING
    )
    tipo_relacion_id = models.ForeignKey(
        Relacion,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)
