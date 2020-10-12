from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path('',views.InicioView.as_view(), name='inicio'),
    path('lista_todo_empleados/',views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('lista_by_departamento/<name>/',views.ListByAreaEmpleados.as_view(), name='empleados_area'),
    path('lista_empleados/',views.ListaEmpleadosAdmin.as_view(), name='admin_empleados'),
    path('buscar_by_kword/',views.ListEmpleadosByKword.as_view()),
    path('listar_habilidades_empleado/',views.ListHabilidadesEmpleado.as_view()),
    path('empleado_detalle/<pk>/', views.EmpledoDetailView.as_view(), name='detalle_empleado'),
    path('add_empleado/', views.CrearEmpleadoView.as_view(), name='add_empleado'),
    path('sucess/', views.SucessView.as_view(), name='correcto'),
    path('actualizar_empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='actualizar_empleado'),
    path('eliminar_empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
]   

