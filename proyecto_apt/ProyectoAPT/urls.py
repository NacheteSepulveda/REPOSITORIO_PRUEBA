"""
URL configuration for proyecto_apt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Setup include to allow other app's urls to 
from . import views # COMO QUE NO EXISTE? XD

from django.conf import settings
from django.conf.urls.static import static
from .views import *
from ProyectoAPT.views import filtrar_estudiantes


urlpatterns = [
    path('', views.index, name='index'),
    # Horarios
    path('horarios/', views.registroHoras, name='horarios'),
    path('Horarios/<int:estudianteID>', views.tratamientosForm, name='tratamientosEstudiante'),
    # There we will enable the horario LIST
    path('obtener-horarios-disponibles/', views.obtener_horarios_disponibles, name='obtener_horarios_disponibles'),

    # Eliminar horario
    path('eliminar-horario/<int:id>/', views.eliminar_horario, name='eliminar_horario'),



    # AUTH
    path('login/', views.loginUser, name='login'),
    path('registro/', views.register, name='registro'),
    path('logout/', views.custom_logout, name='logout'),

    #Servicios
    path('servicios/', views.servicios, name='servicios'),

    

    #Citas Paciente
    path('citas/', views.citas_pac, name='citas'),
    path('filtrar-estudiantes/', views.filtrar_estudiantes, name='filtrar_estudiantes'),

    # Añadir a subPage de Estudiante....
    path('estudiante/infopersonal/', views.infoestudiante, name="infoestudiante"),
    path('estudiante/notificaciones_estudiante/', views.notifiaciones_est, name="notificaciones"),
    path('estudiante/pacientes_estudiante/', views.pacientes_est, name="pacientes_est"),
    path('estudiante/calendario_est/',  views.calendar_est, name="calendario"), 
    path('crear_historial_medico/<int:paciente_id>/', views.crear_historial_medico, name='crear_historial_medico'),

    #crear ficha paciente
    path('crear-ficha/<int:user_id>/', views.crear_ficha_paciente, name='crear_ficha_paciente'),
    path('lista_fichas_clinicas/', views.ver_ficha_clinica, name='lista_fichas_clinicas'),
    path('horarios/', filtrar_estudiantes, name='horarios'),   
    path('ver_ficha_clinica/<int:paciente_id>/', views.ver_ficha_clinica, name='ver_ficha_clinica')


    

]
# Solo en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)