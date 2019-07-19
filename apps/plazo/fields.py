# apps/plazo/fields.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import PrimaryKeyRelatedField


# Local imports
from .models import Plazo
from .serializers import PlazoSerializer


# Create your serializers here.
class PlazoField(PrimaryKeyRelatedField):
    queryset = Plazo.objects.all()

    def to_representation(self, value):
        instance = self.get_queryset().get(pk=value.pk)
        serializer = PlazoSerializer(instance)
        return serializer.data
