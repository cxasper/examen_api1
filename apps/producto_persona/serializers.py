# apps/producto_persona/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Producto_persona


# Create your serializers here.
class Producto_personaSerializer(ModelSerializer):

    class Meta:
        model = Producto_persona
        fields = '__all__'
