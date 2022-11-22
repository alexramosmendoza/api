
from ferreteria.serializer import *
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class Empleado_view(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = Empleado_serializer

class Cliente_view(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = Cliente_serializer

class Proveedor_view(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = Proveedor_serializer

class Producto_view(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = Producto_serializer

class Usuario_view(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = Usuario_serializer

class Factura_view(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = Factura_serializer

class Venta_view(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = Venta_serializer

class Compra_view(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = Compra_serializer

class TokenProvider(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        user.token = token.key
        user.save()
        usuario = Usuario_serializer(user)
        return Response(usuario.data)



