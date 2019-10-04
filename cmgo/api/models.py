from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Slide(models.Model):
    name = models.CharField('Nombre', max_length=50)

    def __str__(self):
        return self.name


class SlideImage(models.Model):
    section = models.ForeignKey(Slide, on_delete=models.CASCADE, related_name='slides')
    image = models.ImageField(
        upload_to='slides', help_text='1280 × 518 px')
    url = models.URLField()
    ordering = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['ordering']





# class Event(models.Model):
#     number = models.PositiveIntegerField('Número')
#     title = models.CharField('Título', max_length=100)
#     start_date = models.DateTimeField('Fecha Inicio')
#     end_date = models.DateTimeField('Fecha Fin')
#     responsable = models.CharField('Responsable', max_length=100)
#     institution = models.CharField('Institución', max_length=100)
#     phone = models.CharField('Teléfono', max_length=50)
#     email = models.CharField('Correo', max_length=50)
#     points_holder = models.PositiveIntegerField()
#     # points_holder
#     # PUNTAJE PARA EL TITULAR DEL CURSO

    
#     academic_program_url = models.URLField('Url Programa Académico', blank=True, max_length=500)
#     inscription_url = models.URLField('Url Inscripción', blank=True, max_length=500)
#     ordering = models.PositiveSmallIntegerField(default=0)
#     month = models.CharField(max_length=50, null=False, blank=True, default='')

#     class Meta:
#         verbose_name_plural = 'Actividades'
#         ordering = ['start_date', 'ordering']

#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         self.month = self.start_date.strftime("%B")
#         super(Actividad, self).save(*args, **kwargs)
