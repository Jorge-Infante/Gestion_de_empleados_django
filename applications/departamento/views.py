from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import(
    ListView
)
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento

class ListaDepartamentoListView(ListView):
    template_name="departamento/lista_departamento.html"
    model = Departamento
    context_object_name ='departamento'
    
    

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    
    def form_valid(self, form):
        
        depa= Departamento(
            name=form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shortname']  
        )
        depa.save()
        
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellidos,
            job='1',
            departamento=depa,
            
        )
        return super(NewDepartamentoView,self).form_valid(form)