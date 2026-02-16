from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Publicacion, Comentario 
from .forms import FormPublicacion, FormComentario 
from django.contrib import messages 

def lista_public(request):
    usuarioActivo = request.user
    publicaciones = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    return render(request, 'blog/lista_public.html', 
    {'publicaciones': publicaciones, 'usuarioActivo':usuarioActivo,})

def nueva_public(request):
    if request.method == "POST":
        form = FormPublicacion(request.POST)
        if form.is_valid():
            pub = form.save(commit=False)
            pub.autor = request.user
            pub.fecha_publicacion = timezone.now()
            pub.save()
            return redirect('lista_public')
    else:
        form = FormPublicacion()
    return render(request, 'blog/editar_public.html', {'form': form})

def editar_public(request, pk):
    pub = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = FormPublicacion(request.POST, instance=pub)
        if form.is_valid():
            pub = form.save(commit=False)
            pub.autor = request.user
            pub.fecha_publicacion = timezone.now()
            pub.save()
            return redirect('lista_public')
    else:
        form = FormComentario() # Ojo: acá debe decir FormPublicacion(instance=pub)
        form = FormPublicacion(instance=pub)
    return render(request, 'blog/editar_public.html', {'form': form})


def detalle_public(request, pk):

    publicacion = get_object_or_404(Publicacion, pk=pk)
    
    if request.method == "POST":

        form = FormComentario(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.publicacion = publicacion
            comentario.save()
            
            messages.success(request, '¡Comentario publicado con éxito!')
            
            return redirect('detalle_public', pk=publicacion.pk)
    else:
        form = FormComentario()
        
    return render(request, 'blog/detalle_public.html', {
        'publicacion': publicacion, 
        'form': form, 
        'usuarioActivo': request.user
    })

    