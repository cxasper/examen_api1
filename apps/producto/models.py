# apps/producto/models.py
# Python imports


# Django imports
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
# Third party apps imports


# Local imports
from apps.credito.models import Credito
from apps.plazo.models import Plazo
# Create your models here.
class Producto(models.Model):
    tipo_credito_id = models.ForeignKey(
        Credito,
        on_delete=models.DO_NOTHING
    )
    plazo_id = models.ForeignKey(
        Plazo,
        on_delete=models.DO_NOTHING
    )
    numero_credito = models.CharField(
        max_length=45,
        validators=[RegexValidator(r'^\d{0,9}$')],
    )
    numero_cuotas = models.IntegerField(validators=[MinValueValidator(1)])
    saldo = models.CharField(
        max_length=45,
        validators=[RegexValidator(r'^\d{0,9}$')],
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)
