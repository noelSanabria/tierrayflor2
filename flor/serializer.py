from rest_framework import serializers
from flor.models import Usuario, Direccion, Rol, Comuna, Region, Venta, Pregunta, Detalle, Producto, Categoria

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'correo', 'direccion', 'apellido', 'rut', 'nombre', 'clave', 'telefono']

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['id_direccion', 'calle', 'numero']

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id_rol', 'nombre']

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id_comuna']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id_region', 'nombre']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['id_venta', 'f_venta', 'f_entrega', 'total', 'carrito', 'estatus']

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ['id_pregunta', 'pregunta']

class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = ['id_detalle', 'cantidad', 'subtotal']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre', 'descripcion', 'precio', 'stock']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id_categoria', 'nombre']     