from django.urls import path,include
from ferreteria.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('empleado', Empleado_view,basename='empleado')
router.register('cliente', Cliente_view,basename='cliente')
router.register('proveedor', Proveedor_view,basename='proveedor')
router.register('producto', Producto_view,basename='producto')
router.register('usuario', Usuario_view,basename='usuario')
router.register('factura', Factura_view,basename='factura')
router.register('venta', Venta_view,basename='venta')
router.register('compra', Compra_view,basename= 'compra')

urlpatterns = [
    path('', include(router.urls)),
    path('token',TokenProvider.as_view(),name='token')


]
