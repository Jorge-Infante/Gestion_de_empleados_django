from django.contrib import admin
from .models import Empleado, Habilidades
admin.site.register(Habilidades)
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display =(
        'first_name',
        'last_name',
        'departamento',
        'job',
        'fullname',
        
    )
    
    def fullname(self,obj):
        return obj.first_name+ ' ' +obj.last_name
    
    
    
    #
    search_fields =('first_name',)
    list_filter = ('job','habilidad')
    #
    filter_horizontal = ('habilidad',)
    
admin.site.register(Empleado,EmpleadoAdmin)