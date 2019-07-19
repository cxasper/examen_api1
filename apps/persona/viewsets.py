# apps/persona/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

# Local imports
from .serializers import PersonaSerializer
from .models import Persona


# Create your viewsets here.
class PersonaViewSet(ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
