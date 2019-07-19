# apps/plazo/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .serializers import PlazoSerializer
from .models import Plazo


# Create your viewsets here.
class PlazoViewSet(ModelViewSet):
    queryset = Plazo.objects.all()
    serializer_class = PlazoSerializer
