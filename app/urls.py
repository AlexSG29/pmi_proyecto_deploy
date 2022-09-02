from django.urls import path
from . import views 

from django.contrib.auth import views as auth_views


app_name = 'pmi'
urlpatterns = [
    path('', views.tareas_lista, name='tareas'),
    path('adelantos/', views.adelantos_lista, name='adelantos'),
    #path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #crear
    path('crear_tarea/', views.crear_tarea, name='crear-tarea'),
    path('crear_adelanto/', views.crear_adelanto, name='crear-adelanto'),
    #editar
    path('editar_tarea/<int:id>', views.editar_tarea, name='editar-tarea'),
    path('editar_adelanto/<int:id>', views.editar_adelanto, name='editar-adelanto'),

]