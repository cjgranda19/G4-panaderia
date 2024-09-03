from rest_framework import viewsets
from .models import Categoria
from .serializers import CategoriaSerializer

from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import path
from .models import Categoria

# Create your views here.
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

def confirm_update(request, obj_id):
    if request.method == 'POST':
        if 'confirm' in request.POST:
            categoria = Categoria.objects.get(id=obj_id)
            form = CategoriaAdmin.form(request.POST, instance=categoria)
            if form.is_valid():
                form.save()
                messages.success(request, 'Category updated successfully.')
                return redirect('admin:my_app_categoria_changelist')
        else:
            messages.info(request, 'Category update canceled.')
            return redirect('admin:my_app_categoria_changelist')
    return render(request, 'confirm_update.html', {'obj_id': obj_id})