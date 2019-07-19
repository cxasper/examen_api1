# apps/producto_persona/fields.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import PrimaryKeyRelatedField


# Local imports
from .models import Producto_persona
from .serializers import Producto_personaSerializer


# Create your serializers here.
class Producto_personaField(PrimaryKeyRelatedField):
    queryset = Producto_persona.objects.all()

    def to_representation(self, value):
        instance = self.get_queryset().get(pk=value.pk)
        serializer = Producto_personaSerializer(instance)
        return serializer.data
