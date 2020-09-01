from django.shortcuts import render
from rest_framework import viewsets
from .models import Anuncio, Categoria, Habilidad, Facultad,Persona,Consumidor,Sugerencia,Noticia,Administrador,User
from .serializers import AnuncioSerializer,CategoriaSerializer,HabilidadSerializer, FacultadSerializer,PersonaSerializer,ConsumidorSerializer,SugerenciaSerializer, NoticiaSerializer,AdministradorSerializer,UserSerializer



class PersonaViewSet(viewsets.ModelViewSet):
    serializer_class=PersonaSerializer
    queryset=Persona.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()


class AnuncioViewSet(viewsets.ModelViewSet):
    serializer_class=AnuncioSerializer
    queryset=Anuncio.objects.all()

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class=CategoriaSerializer
    queryset=Categoria.objects.all()

class HabilidadViewSet(viewsets.ModelViewSet):
    serializer_class=HabilidadSerializer
    queryset=Habilidad.objects.all()

class FacultadViewSet(viewsets.ModelViewSet):
    serializer_class=FacultadSerializer
    queryset=Facultad.objects.all()


class ConsumidorViewSet(viewsets.ModelViewSet):
    serializer_class=ConsumidorSerializer
    queryset=Consumidor.objects.all()

class SugerenciaViewSet(viewsets.ModelViewSet):
    serializer_class=SugerenciaSerializer
    queryset=Sugerencia.objects.all()

class NoticiaViewSet(viewsets.ModelViewSet):
    serializer_class=NoticiaSerializer
    queryset=Noticia.objects.all()

class AdministradorViewSet(viewsets.ModelViewSet):
    serializer_class=AdministradorSerializer
    queryset=Administrador.objects.all()
