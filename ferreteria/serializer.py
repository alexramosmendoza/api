from rest_framework import serializers
from ferreteria.models import *

class Empleado_serializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class Cliente_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class Proveedor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class Producto_serializer(serializers.ModelSerializer):
    proveedor = Proveedor_serializer(read_only=True)
    proveedor_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Proveedor.objects.all(),source='proveedor')
    class Meta:
        model = Producto
        fields = '__all__'

class Usuario_serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            correo=validated_data['correo'],
            telefono=validated_data['telefono'],
            nombre=validated_data['nombre'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class Factura_serializer(serializers.ModelSerializer):
    cliente = Cliente_serializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Cliente.objects.all(),source='cliente')
    empleado = Empleado_serializer(read_only=True)
    empleado_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Empleado.objects.all(),source='empleado')
    producto = Producto_serializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(),source='producto')
    class Meta:
        model = Factura
        fields = '__all__'

class Venta_serializer(serializers.ModelSerializer):
    factura = Factura_serializer(read_only=True)
    factura_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Factura.objects.all(),source='factura')
    producto = Producto_serializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(),source='producto')
    class Meta:
        model = Venta
        fields = '__all__'

class Compra_serializer(serializers.ModelSerializer):
    producto = Producto_serializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Producto.objects.all(),source='producto')
    proveedor = Proveedor_serializer(read_only=True)
    proveedor_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Proveedor.objects.all(),source='proveedor')
    class Meta:
        model = Compra
        fields = '__all__'
