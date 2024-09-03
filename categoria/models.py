from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        error_messages={
            'unique': 'Advertencia: La categoría ya ha sido añadida antes',
            'null': 'Error: Por favor, complete todos los campos obligatorios para continuar',
            'blank': 'Error: Por favor, complete todos los campos obligatorios para continuar',
        }
    )
    descripcion = models.TextField(
        null=False,
        blank=False,
        error_messages={
            'null': 'Error: Por favor, complete todos los campos obligatorios para continuar',
            'blank': 'Error: Por favor, complete todos los campos obligatorios para continuar',
        }
    )
    imagen = models.ImageField(
        'imagen',
        upload_to='categoria',
        null=False,
        blank=False,
        error_messages={
            'null': 'Error: Por favor, complete todos los campos obligatorios para continuar',
            'blank': 'Error: Por favor, complete todos los campos obligatorios para continuar',
        }
    )

    def __str__(self):
        return self.nombre

models.export = [Categoria]
