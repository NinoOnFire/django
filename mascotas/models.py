from django.db import models
from django.contrib.auth.models import User

class Mascotas(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto= models.ImageField(upload_to='images/')

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.raza, self.descripcion)
    
    class Meta():
        db_table = 'mascota'
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

class Cliente(models.Model):
    Run_Cliente = models.CharField(max_length=10, primary_key=True)
    Nombre_Cliente = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Correo = models.TextField()
    Telefono = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.Nombre_Cliente} {self.Apellido}"


class Solicitud(models.Model):
    Id = models.AutoField(primary_key=True)
    Run_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Nombre_Mascota = models.ForeignKey(Mascotas, on_delete=models.CASCADE)
    Detalle = models.TextField()
    Fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud {self.Id} - {self.Run_Cliente}"


