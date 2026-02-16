from django import forms
from .models import Publicacion
from .models import Publicacion, Comentario 

class FormPublicacion(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ('titulo', 'texto',)


class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto',) 