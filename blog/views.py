from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion

def lista_public(request):
   
    publicaciones = Publicacion.objects.filter(   # 1. Hacemos la consulta a la base de datos (el query)
        fecha_publicacion__lte=timezone.now()
    ).order_by('fecha_publicacion')
    
    return render(request, 'blog/lista_public.html', {'publicaciones': publicaciones}) # 2. Renderizamos y pasamos el diccionario de contexto {'clave': valor}