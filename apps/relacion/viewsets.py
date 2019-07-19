# apps/relacion/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .serializers import RelacionSerializer
from .models import Relacion


# Create your viewsets here.
class RelacionViewSet(ModelViewSet):
    queryset = Relacion.objects.all()
    serializer_class = RelacionSerializer
