# apps/credito/fields.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import PrimaryKeyRelatedField


# Local imports
from .models import Credito
from .serializers import CreditoSerializer


# Create your serializers here.
class CreditoField(PrimaryKeyRelatedField):
    queryset = Credito.objects.all()

    def to_representation(self, value):
        instance = self.get_queryset().get(pk=value.pk)
        serializer = CreditoSerializer(instance)
        return serializer.data
