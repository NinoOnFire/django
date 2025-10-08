from django.shortcuts import render, redirect
from mascotas.models import Mascotas
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .froms import ClienteForm, SolicitudForm
from .models import Solicitud

# Create your views here.

def galeria(request):
    mascotas = Mascotas.objects.all()
    data = {'mascotas': mascotas }
    return render(request, 'galeria.html', data)

def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def crear_cliente_y_solicitud(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        solicitud_form = SolicitudForm(request.POST)

        if cliente_form.is_valid() and solicitud_form.is_valid():
            # Guardamos el cliente
            cliente = cliente_form.save()

            # Creamos la solicitud asociada a ese cliente
            solicitud = solicitud_form.save(commit=False)
            solicitud.Run_Cliente = cliente
            solicitud.save()

            return redirect('solicitudes')  # Cambia por la URL que corresponda

    else:
        cliente_form = ClienteForm()
        solicitud_form = SolicitudForm()

    context = {
        'cliente_form': cliente_form,
        'solicitud_form': solicitud_form
    }
    return render(request, 'solicitud.html', context)

def lista_solicitudes(request):
    solicitudes = Solicitud.objects.all().order_by('-Fecha')
    context = {'solicitudes': solicitudes}
    return render(request, 'solicitudes.html', context)