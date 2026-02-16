from django.conf import settings
from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    publicacion = models.ForeignKey('blog.Publicacion', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.texto