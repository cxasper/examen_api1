# apps/relacion/fields.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import PrimaryKeyRelatedField


# Local imports
from .models import Relacion
from .serializers import RelacionSerializer


# Create your serializers here.
class RelacionField(PrimaryKeyRelatedField):
    queryset = Relacion.objects.all()

    def to_representation(self, value):
        instance = self.get_queryset().get(pk=value.pk)
        serializer = RelacionSerializer(instance)
        return serializer.data
