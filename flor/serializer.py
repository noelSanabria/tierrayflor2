from rest_framework import serializer
from flor.models import usuario
from flor.models import rol
class usuarioserializer(serializer,modelserializer):
    class metas:
        model = usuario
        fields=['id_usuario','correo','direccion','apellido',
                'rut','nombre','clave','telefono']
        
class rolserializer(serializer,modelserializer):
    class metas:
        model = rol
        fields=['id_rol','nombre']        