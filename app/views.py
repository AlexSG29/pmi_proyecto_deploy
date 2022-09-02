from django.shortcuts import render, redirect
from .models import Tarea, Adelanto 
#Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#login
""" from django.contrib.auth import authenticate, login
from .forms import LoginForm """
from django.contrib.auth.decorators import login_required
#formularios
from .forms import TareaForm, AdelantoForm


def tareas_lista (request):
    tareas = Tarea.objects.all()
    #Paginacion
    paginator = Paginator(tareas, 6)
    page = request.GET.get('page')
    try:
        tareas = paginator.page(page)
    except PageNotAnInteger:
        tareas = paginator.page(1)
    except EmptyPage:
        tareas = paginator.page(paginator.num_pages)
    return render(request, 'paginas/tareas.html',
                    {'tareas': tareas,
                    'page': page },
                )
                

def adelantos_lista (request):
    adelantos = Adelanto.objects.all()
    #Paginacion
    paginator = Paginator(adelantos, 10)
    page = request.GET.get('page')
    try:
        adelantos = paginator.page(page)
    except PageNotAnInteger:
        adelantos = paginator.page(1)
    except EmptyPage:
        adelantos = paginator.page(paginator.num_pages)
    return render(request, 'paginas/adelantos.html',
                    {'adelantos': adelantos,
                    'page': page},
                )

@login_required
def crear_tarea (request):
    formulario = TareaForm(request.POST or None) 
    if formulario.is_valid():
        formulario.save()
        return redirect('pmi:tareas')
    return render(request, 'formularios/tarea_crear.html',
                    {'formulario': formulario},
                )

@login_required
def crear_adelanto (request):
    formulario = AdelantoForm(request.POST or None) 
    if formulario.is_valid():
        formulario.save()
        return redirect('pmi:adelantos')
    return render(request, 'formularios/adelanto_crear.html',
                    {'formulario': formulario},
                )

@login_required
def editar_tarea (request, id):
    tarea = Tarea.objects.get(id=id)
    formulario = TareaForm(request.POST or None, instance=tarea)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('pmi:tareas')

    return render(request, 'formularios/editar_tarea.html',
                    {'formulario': formulario,})

@login_required
def editar_adelanto (request, id):
    adelanto = Adelanto.objects.get(id=id)
    formulario = AdelantoForm(request.POST or None, instance=adelanto)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('pmi:adelantos')

    return render(request, 'formularios/editar_adelanto.html',
                    {'formulario': formulario,})