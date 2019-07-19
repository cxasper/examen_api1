# apps/persona/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import PersonaViewSet


# Create your routers here.
persona = (
    (r'personas', PersonaViewSet),
)
