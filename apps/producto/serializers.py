# apps/producto/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Producto


# Create your serializers here.
class ProductoSerializer(ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'
