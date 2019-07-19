# apps/credito/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import CreditoViewSet


# Create your routers here.
credito = (
    (r'tipo-creditos', CreditoViewSet),
)
