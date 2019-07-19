# apps/producto/fields.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import PrimaryKeyRelatedField


# Local imports
from .models import Producto
from .serializers import ProductoSerializer


# Create your serializers here.
class ProductoField(PrimaryKeyRelatedField):
    queryset = Producto.objects.all()

    def to_representation(self, value):
        instance = self.get_queryset().get(pk=value.pk)
        serializer = ProductoSerializer(instance)
        return serializer.data
