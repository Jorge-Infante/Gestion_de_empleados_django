from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,

)

# import modelo empleado
from .models import Empleado
from .models import Habilidades
class InicioView(TemplateView):
    """Pagina de inicio"""
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name="persona/list_all.html"
    paginate_by = 4   #Agregar paginacion
   
    
    def get_queryset(self):
        print('****')
        palabra_clave = self.request.GET.get("kword", '')
        lista= Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        
        #print ('lista:',lista)
        return lista
    

class ListByAreaEmpleados(ListView):
    template_name="persona/list_by_area.html"
    context_object_name = 'empleados'
    #modo 1
    #queryset = Empleado.objects.filter(
    #    departamento__name='Reparacion'
    #)
    def get_queryset(self):
        area=self.kwargs['name']
        lista= Empleado.objects.filter(
            departamento__name=area
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name= 'persona/lista_empleados.html' 
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado   


class ListEmpleadosByKword(ListView):
    template_name = "persona/by_kword.html"
    context_object_name = 'empleados'
    
    def get_queryset(self):
        print('****')
        palabra_clave = self.request.GET.get("kword", '')
        lista= Empleado.objects.filter(
            first_name=palabra_clave
        )
        
        #print ('lista:',lista)
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name="persona/habilidades.html"
    context_object_name= 'habilidades'
    
    #def get_queryset(self):
    #    empleado= Empleado.objects.get(id=2)
    #   return empleado.habilidad.all()
     
class EmpledoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    
class SucessView(TemplateView):
    template_name="persona/sucess.html"
    
class CrearEmpleadoView(CreateView):
    template_name= "persona/registrar_empleado.html"
    model = Empleado
    #fields= ('__all__')
    fields= [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidad',
        'avatar',
    ]
    success_url = reverse_lazy('persona_app:correcto')
    
    def form_valid(self, form):
        empleado=form.save(commit=False) #ya se guardó
        empleado.full_name = empleado.first_name + ' '+ empleado.last_name
        empleado.save()
        return super(CrearEmpleadoView, self).form_valid(form)
    
class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields= [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidad',
    ]
    success_url = reverse_lazy('persona_app:admin_empleados')
    #probando post and valid
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('**********POST***********')
        print('******************************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        print('**********VALID***********')
        print('******************************')
        return super(EmpleadoUpdateView, self).form_valid(form)
      

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:correcto')
         