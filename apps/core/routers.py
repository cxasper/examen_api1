# apps/core/routers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.routers import DefaultRouter


# Local imports
# from ..app_django.routers import router_list as app_django_router
from apps.persona.routers import persona
from apps.relacion.routers import relacion
from apps.plazo.routers import plazo
from apps.credito.routers import credito
from apps.producto.routers import producto
from apps.producto_persona.routers import producto_persona
# Create your routers here.
# routers_tuples = (app_django_router,)
routers_tuples = (persona,relacion,plazo,credito,producto,producto_persona,)
routers_lists = sum(
    [list(router_tuple) for router_tuple in routers_tuples], [])

router = DefaultRouter()

for router_list in sorted(routers_lists):
    router.register(router_list[0], router_list[1], base_name=router_list[0])
