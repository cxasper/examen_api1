# apps/plazo/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Plazo


# Create your serializers here.
class PlazoSerializer(ModelSerializer):

    class Meta:
        model = Plazo
        fields = '__all__'
