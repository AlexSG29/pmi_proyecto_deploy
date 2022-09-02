from django.contrib import admin
from .models import Tarea, Adelanto, Estudiante 
# Register your models here.

admin.site.register(Tarea)
admin.site.register(Estudiante)
admin.site.register(Adelanto)