# apps/credito/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Credito


# Create your serializers here.
class CreditoSerializer(ModelSerializer):

    class Meta:
        model = Credito
        fields = '__all__'
