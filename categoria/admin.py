from django.contrib import admin
from .models import Categoria
from django.utils.html import format_html
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'image')
    search_fields = ['nombre', 'descripcion']
    list_filter = ('nombre',)

    def image(self, obj):
        return format_html('<img src={} width=150/>', obj.imagen.url)

    def save_model(self, request, obj, form, change):
        if change:
            response = print('¿Estás seguro de que deseas actualizar la categoría?')
            response = input('Ingresa "si" para confirmar: ')
            if response.lower() == 'si':
                super().save_model(request, obj, form, change)
                messages.success(request, 'Advertencia, la categoría ha sido actualizada')
            else:
                messages.info(request, 'Advertencia, la categoría no ha sido actualizada')
        else:
            super().save_model(request, obj, form, change)


admin.site.register(Categoria, CategoriaAdmin)

