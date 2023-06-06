from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    correo = models.EmailField(max_length=100)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()

    def __str__(self):
        return f"{self.calle}, {self.numero}"

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    # Agrega los campos que necesites para la comuna

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    f_venta = models.DateField()
    f_entrega = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    carrito = models.TextField()
    estatus = models.CharField(max_length=100)

    def __str__(self):
        return f"Venta {self.id_venta}"

class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    pregunta = models.TextField()

    def __str__(self):
        return self.pregunta

class Detalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
