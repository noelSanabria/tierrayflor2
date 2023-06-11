from django.contrib import admin
from .models import Usuario, Direccion, Rol, Comuna, Region, Venta, Pregunta, Detalle, Producto, Categoria

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'correo', 'direccion', 'apellido', 'rut', 'nombre', 'telefono')
    list_filter = ('rol',)
    search_fields = ('nombre', 'apellido', 'correo')
    list_per_page = 20
    ordering = ('id_usuario',)

class DireccionAdmin(admin.ModelAdmin):
    list_display = ('id_direccion', 'calle', 'numero')
    search_fields = ('calle', 'numero')
    list_per_page = 20

class RolAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'nombre')
    search_fields = ('nombre',)
    list_per_page = 20

class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id_comuna',)
    search_fields = ('id_comuna',)
    list_per_page = 20

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id_region', 'nombre')
    search_fields = ('nombre',)
    list_per_page = 20

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id_venta', 'f_venta', 'f_entrega', 'total', 'carrito', 'estatus')
    search_fields = ('id_venta',)
    list_per_page = 20

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('id_pregunta', 'pregunta')
    search_fields = ('pregunta',)
    list_per_page = 20

class DetalleAdmin(admin.ModelAdmin):
    list_display = ('id_detalle', 'cantidad', 'subtotal')
    search_fields = ('id_detalle',)
    list_per_page = 20

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'descripcion', 'precio', 'stock')
    list_filter = ('categoria',)
    search_fields = ('nombre',)
    list_per_page = 20

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre')
    search_fields = ('nombre',)
    list_per_page = 20

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Direccion, DireccionAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Detalle, DetalleAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)