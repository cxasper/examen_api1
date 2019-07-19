# apps/persona/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
# Local imports
from .models import Persona
from apps.producto_persona.serializers import Producto_personaSerializer
from apps.producto_persona.models import Producto_persona
# Create your serializers here.
class PersonaSerializer(ModelSerializer):

    class Meta:
        model = Persona
        fields = '__all__'

class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'

class VendorSerializer(ModelSerializer):

    class Meta:
        model = Vendor
        fields = '__all__'

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Persona
        fields = '__all__'

class FactSerializer(ModelSerializer):

    class Meta:
        model = Persona
        fields = '__all__'

class DetailFactSerializer(ModelSerializer):

    class Meta:
        model = Persona
        fields = '__all__'
