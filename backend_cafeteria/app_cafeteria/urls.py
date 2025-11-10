from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/ver/', views.ver_empleado, name='ver_empleado'),
    path('empleados/actualizar/<int:pk>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleados/borrar/<int:pk>/', views.borrar_empleado, name='borrar_empleado'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/ver/', views.ver_cliente, name='ver_cliente'),
    path('clientes/actualizar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),
]
