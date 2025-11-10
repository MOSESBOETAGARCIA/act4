from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Cliente

def home(request):
    return render(request, 'home.html')

def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        id_empleado = request.POST['id_empleado']
        puesto = request.POST['puesto']
        salario = request.POST['salario']
        disponible = request.POST.get('disponible', False) == 'on'
        fecha_contratacion = request.POST['fecha_contratacion']
        Empleado.objects.create(
            nombre=nombre,
            id_empleado=id_empleado,
            puesto=puesto,
            salario=salario,
            disponible=disponible,
            fecha_contratacion=fecha_contratacion
        )
        return redirect('ver_empleado')
    return render(request, 'empleado/agregar_empleado.html')

def ver_empleado(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})

def actualizar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.id_empleado = request.POST['id_empleado']
        empleado.puesto = request.POST['puesto']
        empleado.salario = request.POST['salario']
        empleado.disponible = request.POST.get('disponible', False) == 'on'
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.save()
        return redirect('ver_empleado')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def realizar_actualizacion_empleado(request, pk):
    return actualizar_empleado(request, pk)

def borrar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleado')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        activo = request.POST.get('activo', False) == 'on'
        direccion = request.POST.get('direccion', '')
        fecha_nacimiento = request.POST.get('fecha_nacimiento', None)
        genero = request.POST.get('genero', '')
        preferencias = request.POST.get('preferencias', '')
        Cliente.objects.create(
            nombre=nombre,
            email=email,
            telefono=telefono,
            activo=activo,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento if fecha_nacimiento else None,
            genero=genero,
            preferencias=preferencias
        )
        return redirect('ver_cliente')
    return render(request, 'cliente/agregar_cliente.html')

def ver_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})

def actualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.email = request.POST['email']
        cliente.telefono = request.POST['telefono']
        cliente.activo = request.POST.get('activo', False) == 'on'
        cliente.direccion = request.POST.get('direccion', '')
        cliente.fecha_nacimiento = request.POST.get('fecha_nacimiento', None)
        cliente.genero = request.POST.get('genero', '')
        cliente.preferencias = request.POST.get('preferencias', '')
        cliente.save()
        return redirect('ver_cliente')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, pk):
    return actualizar_cliente(request, pk)

def borrar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})
