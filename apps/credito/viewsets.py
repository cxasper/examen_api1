# apps/credito/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .serializers import CreditoSerializer
from .models import Credito


# Create your viewsets here.
class CreditoViewSet(ModelViewSet):
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer
