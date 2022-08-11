from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import MarcaViewset, contactos, home, contactos, galeria, agregar_producto, \
    listar_productos, modificar_producto, eliminar_producto, registro, ProductoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('marca', MarcaViewset)

urlpatterns = [
    path('', home, name='home'),
    path('contactos/', contactos, name='contactos'),
    path('galeria/', galeria, name='galeria'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('listar-productos/', listar_productos, name='listar_productos'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', eliminar_producto, name='eliminar_producto'),
    path('registro/', registro, name='registro'),
    path('api/', include(router.urls))
]