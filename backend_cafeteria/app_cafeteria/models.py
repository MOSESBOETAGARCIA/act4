from django.db import models

# ==========================================
# MODELO: EMPLEADO
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    id_empleado = models.PositiveIntegerField(unique=True)
    puesto = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f"Empleado {self.id_empleado} - {self.nombre}"

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    fecha_registro = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    direccion = models.CharField(max_length=200, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], blank=True)
    preferencias = models.TextField(blank=True)

    def __str__(self):
        return f"Cliente {self.nombre} - {self.email}"
