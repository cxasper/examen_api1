# apps/relacion/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Relacion


# Create your serializers here.
class RelacionSerializer(ModelSerializer):

    class Meta:
        model = Relacion
        fields = '__all__'
