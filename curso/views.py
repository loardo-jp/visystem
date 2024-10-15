from django.shortcuts import render, redirect, get_object_or_404
from .models import curso
from .forms import CursoForm

# Vista para listar los cursos
def get_curso(request):
    cursos = curso.objects.all()
    return render(request, 'lista_cursos.html', {
        'title': 'cursos',
        'cursos': cursos,
    })

# Vista para agregar o editar cursos
def formulario(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo curso
            return redirect('lista-cursos')  # Redirige a la página de lista de cursos después de guardar
    else:
        form = CursoForm()

    return render(request, 'formulario_curso.html', {'form': form})

# Vista para editar cursos
def editar_curso(request, curso_id):
    curso_instance = get_object_or_404(curso, id=curso_id)
    
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso_instance)
        if form.is_valid():
            form.save()
            return redirect('lista-cursos')
    else:
        form = CursoForm(instance=curso_instance)

    return render(request, 'formulario_curso.html', {'form': form})

def eliminar_curso(request, curso_id):
    curso_instance = get_object_or_404(curso, id=curso_id)
    curso_instance.delete()  
    return redirect('lista-cursos')     
