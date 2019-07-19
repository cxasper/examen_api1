# apps/producto_persona/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import Producto_personaViewSet


# Create your routers here.
producto_persona = (
    (r'producto-persona', Producto_personaViewSet),
)
