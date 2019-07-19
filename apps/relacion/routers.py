# apps/relacion/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import RelacionViewSet


# Create your routers here.
relacion = (
    (r'tipo-relacion', RelacionViewSet),
)
