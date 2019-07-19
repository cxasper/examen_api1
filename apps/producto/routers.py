# apps/producto/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import ProductoViewSet


# Create your routers here.
producto = (
    (r'productos', ProductoViewSet),
)
