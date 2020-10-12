from django.db import models
from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidades', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleados'
 
    def __str__(self):
        return str(self.id)+' - '+self.habilidad
     


# Create your models here.
class Empleado(models.Model):
    """Modelo para tabla empleado"""
    JOB_CHOICES=(
        ('0', "CONTADOR"),
        ('1', "ADMINISTRADOR"),
        ('2', "ECONOMISTA"),
        ('3', "OTRO"),
    )
    
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombres completos', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)    
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True )
    habilidad = models.ManyToManyField(Habilidades)
   
    def __str__(self):
        return str(self.id)+' - '+self.first_name + ' - ' + self.last_name
        
    