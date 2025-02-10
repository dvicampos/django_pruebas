from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona
from .forms import PersonaForm

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'persona_list.html', {'personas': personas})

def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'persona_form.html', {'form': form})

def editar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'persona_form.html', {'form': form})

def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    if request.method == 'POST':
        persona.delete()
        return redirect('lista_personas')
    return render(request, 'persona_confirm_delete.html', {'persona': persona})
