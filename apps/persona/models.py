# apps/persona/models.py
# Python imports


# Django imports
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Third party apps imports
from django.core.validators import RegexValidator

# Local imports

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    direccion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)

class Vendor(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.TextField(blank=True, null=True)
    numero_dni = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{0,10}$')])
    telefono = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{0,10}$')])
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)

class Client(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.TextField(blank=True, null=True)
    numero_dni = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{0,10}$')])
    telefono = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{0,10}$')])
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)

class Product(models.Model):
    nombre = models.CharField(max_length=100)
    codigo_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField(
        default=1,
        validators=[MinValueValidator(0)])
    precio = models.FloatField(
        validators=[MinValueValidator(0.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)

class Fact(models.Model):
    client_id = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )
    vendor_id = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE
    )
    numero_factura = models.CharField(max_length=100)
    fecha = models.DateField()
    precio_total = models.FloatField(
        validators=[MinValueValidator(0.0)])

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)

class DetailFact(models.Model):
    fact_id = models.ForeignKey(
        Fact,
        on_delete=models.CASCADE
    )
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    cantidad = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)])
    precio = models.FloatField(
        validators=[MinValueValidator(0.0)])

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)
