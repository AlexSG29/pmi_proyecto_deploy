from django.db import models
from django.utils import timezone
# Create your models here.


class Estudiante (models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return (self.nombre)


class Tarea (models.Model):
    ESTADO_CHOICES = [
        ('en curso', 'En Curso'), 
        ('finalizada', 'Finalizada'),  
    ]
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    fecha_inicio = models.DateField(default= timezone.now, verbose_name='Fecha de inicio')
    fecha_fin = models.DateField(default= timezone.now, verbose_name='Fecha final')
    estado = models.CharField(max_length=15, 
                            choices=ESTADO_CHOICES,
                            default='en curso'
                            )
    estudiantes = models.ManyToManyField(Estudiante, blank=True, verbose_name='Responsables')
    class Meta:
        ordering = ('fecha_inicio',)
    
    def __str__(self):
        return (f'{self.titulo} - {self.estado}')

class Adelanto (models.Model):
    tarea = models.ForeignKey(Tarea, 
                            on_delete= models.CASCADE,
                            blank=True,
                            verbose_name='Tarea asignada'
                            )
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descripcion = models.TextField( blank=True, verbose_name='Descripción')
    estudiantes = models.ManyToManyField(Estudiante, blank=True, verbose_name='Seleccionar los participantes')
    tiempo = models.IntegerField(blank=False, verbose_name='Duración')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.titulo} - {self.tarea} - {self.tiempo} horas' )
    
    class Meta:
        ordering = ['-fecha']