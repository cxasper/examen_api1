# apps/plazo/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import PlazoViewSet


# Create your routers here.
plazo = (
    (r'plazos', PlazoViewSet),
)
