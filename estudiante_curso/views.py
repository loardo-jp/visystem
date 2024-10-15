from django.shortcuts import render, redirect, get_object_or_404
from .models import EstudianteCurso
from .forms import EstudianteCursoForm
from curso.models import curso  

# Vista para listar estudiantes y cursos
def Estudiante_Curso(request):
    cursos = curso.objects.all()  # Obtener todos los cursos disponibles
    curso_seleccionado = request.GET.get('curso')  # Obtener el curso seleccionado del filtro (si hay)

    if curso_seleccionado:
        estudiantes_cursos = EstudianteCurso.objects.filter(curso=curso_seleccionado)  # Filtrar por curso seleccionado
    else:
        estudiantes_cursos = EstudianteCurso.objects.all()  # Mostrar todos si no se selecciona un curso

    return render(request, 'lista_est_cur.html', {
        'title': 'Relación estudiantes y curso',
        'estudiantes_cursos': estudiantes_cursos,
        'cursos': cursos,  # Pasar los cursos a la plantilla
        'curso_seleccionado': curso_seleccionado  # Pasar el curso seleccionado a la plantilla
    })

# Vista para agregar o editar un estudiante en un curso
def formulario_estudiante_curso(request, estudiante_curso_id=None):
    if estudiante_curso_id:  # Si se proporciona un id, intenta cargar el objeto correspondiente
        estudiante_curso_instance = get_object_or_404(EstudianteCurso, id=estudiante_curso_id)
    else:
        estudiante_curso_instance = None  # No existe si estamos agregando un nuevo registro

    if request.method == 'POST':
        form = EstudianteCursoForm(request.POST, instance=estudiante_curso_instance)
        if form.is_valid():
            form.save()  # Guarda el formulario
            return redirect('lista-estudiantes-cursos')  # Redirige a la lista
    else:
        form = EstudianteCursoForm(instance=estudiante_curso_instance)  # Muestra el formulario

    return render(request, 'formulario_estudiante_curso.html', {'form': form})

# Vista para editar estudiante en curso
def editar_estudiante_curso(request, estudiante_curso_id):
    estudiante_curso_instance = get_object_or_404(EstudianteCurso, id=estudiante_curso_id)
    
    if request.method == 'POST':
        form = EstudianteCursoForm(request.POST, instance=estudiante_curso_instance)
        if form.is_valid():
            form.save()
            return redirect('lista-estudiantes-cursos')
    else:
        form = EstudianteCursoForm(instance=estudiante_curso_instance)

    return render(request, 'formulario_estudiante_curso.html', {'form': form})


# Vista para eliminar estudiante en curso
def eliminar_estudiante_curso(request, estudiante_curso_id):
    estudiante_curso_instance = get_object_or_404(EstudianteCurso, id=estudiante_curso_id)
    estudiante_curso_instance.delete()  
    return redirect('lista-estudiantes-cursos')
