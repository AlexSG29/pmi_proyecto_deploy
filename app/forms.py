from django.forms import *
from .models import Tarea, Adelanto
from django.contrib.auth import views as auth_views


class TareaForm (ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
        widgets = {
            'titulo': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Titulo',
                    'autocomplete': 'off',
                    'autofocus': True,
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Añade una descripcion detallada para el registro'
                }
            ),
            'fecha_inicio': DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'fecha_fin': DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'estado': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'estudiantes': SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            )
        }

class AdelantoForm (ModelForm):
    class Meta:
        model = Adelanto
        fields = '__all__'
        template_name = 'formularios/adelanto_crear.html'

        widgets = {
            'titulo': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Titulo',
                    'autocomplete': 'off',
                    'autofocus': True,
                }
            ),
            'tarea': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Añade una descripcion detallada para el registro'
                }
            ),
            'estudiantes': SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tiempo': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Horas trabajadas'
                }
            )
        }




    
        


    
        