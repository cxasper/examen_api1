# apps/producto_persona/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .serializers import Producto_personaSerializer
from .models import Producto_persona


# Create your viewsets here.
class Producto_personaViewSet(ModelViewSet):
    queryset = Producto_persona.objects.all()
    serializer_class = Producto_personaSerializer
