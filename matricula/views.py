from django.shortcuts import render, redirect, get_object_or_404
from .models import Matricula
from .forms import MatriculaForm  
from curso.models import curso  # Importar el modelo Curso para mostrar la lista de cursos

# Vista para listar las matrículas con filtro por curso
def lista_matriculas(request):
    cursos = curso.objects.all()  # Obtener todos los cursos disponibles
    curso_seleccionado = request.GET.get('curso')  # Obtener el curso seleccionado del filtro

    if curso_seleccionado:
        matriculas = Matricula.objects.filter(estudiante_curso__curso=curso_seleccionado)  # Filtrar por curso seleccionado
    else:
        matriculas = Matricula.objects.all()  # Mostrar todas las matrículas si no se selecciona un curso

    return render(request, 'lista_matricula.html', {
        'title': 'matrículas',
        'matriculas': matriculas,
        'cursos': cursos,  # Pasar los cursos a la plantilla
        'curso_seleccionado': curso_seleccionado  # Pasar el curso seleccionado a la plantilla
    })

# Vista para agregar o editar una matrícula
def formulario_matricula(request, id=None):
    if id:  # Si se proporciona un ID, se está editando una matrícula
        matricula = get_object_or_404(Matricula, id=id)
        form = MatriculaForm(instance=matricula)
    else:
        form = MatriculaForm()

    if request.method == 'POST':
        form = MatriculaForm(request.POST, instance=matricula if id else None)
        if form.is_valid():
            form.save()  
            return redirect('lista-matriculas')  
    return render(request, 'formulario_matricula.html', {'form': form})

# Vista para eliminar una matrícula
def eliminar_matricula(request, id):
    matricula = get_object_or_404(Matricula, id=id)
    matricula.delete()  # Eliminar la matrícula
    return redirect('lista-matriculas')  # Redirige a la lista de matrículas después de eliminar
