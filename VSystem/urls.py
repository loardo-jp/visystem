"""
URL configuration for VSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from mainApp.views import inicio
from persona.views import get_estudiantes, formulario_estudiante, editar_estudiante,eliminar_estudiante, get_profesores,formulario_profesor,editar_profesor,eliminar_profesor
from curso.views import get_curso, formulario, editar_curso, eliminar_curso
from estudiante_curso.views import Estudiante_Curso, formulario_estudiante_curso, eliminar_estudiante_curso,editar_estudiante_curso
from matricula.views import lista_matriculas, formulario_matricula,eliminar_matricula

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name= 'inicio'),
    path('Lista-estudiantes/',get_estudiantes, name='lista-estudiantes'),
    path('Lista-cursos/',get_curso,name='lista-cursos'),
    path('cursos/agregar/', formulario, name='formulario_curso'),
    path('estudiantes/agregar/', formulario_estudiante, name='formulario_estudiante'),
    path('estudiantes-curso/', Estudiante_Curso, name='lista-estudiantes-cursos'),  
    path('estudiantes-curso/agregar/', formulario_estudiante_curso, name='formulario_estudiante_curso'),
    path('matriculas/', lista_matriculas, name='lista-matriculas'), 
    path('matriculas/nueva/', formulario_matricula, name='formulario_matricula'),  
    path('cursos/editar/<int:curso_id>/', editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:curso_id>/', eliminar_curso, name='eliminar_curso'),
    path('matriculas/editar/<int:id>/', formulario_matricula, name='editar_matricula'),  
    path('matriculas/eliminar/<int:id>/', eliminar_matricula, name='eliminar_matricula'), 
    path('estudiantes-cursos/editar/<int:estudiante_curso_id>/', editar_estudiante_curso, name='editar_estudiante_curso'),
    path('estudiantes-cursos/eliminar/<int:estudiante_curso_id>/', eliminar_estudiante_curso, name='eliminar_estudiante_curso'),
    path('estudiantes/editar/<int:estudiante_id>/', editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:estudiante_id>/', eliminar_estudiante, name='eliminar_estudiante'),
    path('profesores/', get_profesores, name='lista-profesores'),
    path('profesores/nuevo/', formulario_profesor, name='formulario_profesor'),
    path('profesores/editar/<int:profesor_id>/', editar_profesor, name='editar_profesor'),
    path('profesores/eliminar/<int:profesor_id>/', eliminar_profesor, name='eliminar_profesor'),
]