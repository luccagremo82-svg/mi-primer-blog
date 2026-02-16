from django.urls import path
from . import views

urlpatterns = [
path('', views.lista_public, name='lista_public'),
path('publicacion/nueva/', views.nueva_public, name='nueva_public'),
path('publicaciones/<int:pk>/editar/', views.editar_public, name='editar_public'),
]




