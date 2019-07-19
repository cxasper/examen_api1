# apps/persona/fields.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import PrimaryKeyRelatedField


# Local imports
from .models import Persona
from .serializers import PersonaSerializer


# Create your serializers here.
class PersonaField(PrimaryKeyRelatedField):
    queryset = Persona.objects.all()

    def to_representation(self, value):
        instance = self.get_queryset().get(pk=value.pk)
        serializer = PersonaSerializer(instance)
        return serializer.data
