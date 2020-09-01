from rest_framework import serializers
from .models import Anuncio, Categoria, Habilidad, Facultad,Persona,Consumidor,Sugerencia,Noticia,Administrador,User


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class HabilidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Habilidad
        fields=['id','nombre']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields='__all__'

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Facultad
        fields='__all__'



class AdministradorSerializer(serializers.ModelSerializer):
    id= PersonaSerializer(read_only=True)
    class Meta:
        model=Administrador
        fields=['id','rol']

class ConsumidorSerializer(serializers.ModelSerializer):
    id=PersonaSerializer(read_only=True)
    habilidad = HabilidadSerializer(many=True)
    class Meta:
        model=Consumidor
        fields=['id','descripcion','foto','facultad','habilidad']

    

    def create(self, validated_data):
        habilidades_datos = validated_data.pop('habilidad')
        consumidor = Consumidor.objects.create(**validated_data)

        for habil in habilidades_datos:
            habil, created = Habilidad.objects.get_or_create(nombre=habil['nombre'])
            consumidor.habilidad.add(habil)
        return consumidor

    def update(self, instance, validated_data):
        lista_habilidades=[]
        habilidades_datos = validated_data.pop('habilidad')

        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.foto = validated_data.get('foto', instance.foto)
        instance.facultad = validated_data.get('facultad', instance.facultad)

        for habil in habilidades_datos:
            habil, created = Habilidad.objects.get_or_create(nombre=habil['nombre'])
            lista_habilidades.append(habil)
        instance.habilidad.set(lista_habilidades)
        instance.save()
        return instance


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Anuncio
        fields=['id','nombre','descripcion','habilidad','banner','estado','fecha_inicio','fecha_termino','vacantes','cant_interesados','categoria']
     
    habilidad = HabilidadSerializer(many=True)
    
    def create(self, validated_data):

        habilidades_datos = validated_data.pop('habilidad')
        anuncio = Anuncio.objects.create(**validated_data)

        for habil in habilidades_datos:
            habil, created = Habilidad.objects.get_or_create(nombre=habil['nombre'])
            anuncio.habilidad.add(habil)
        return anuncio

    def update(self, instance, validated_data):
        lista_habilidades=[]
        habilidades_datos = validated_data.pop('habilidad')
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.banner = validated_data.get('banner', instance.banner)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.fecha_termino = validated_data.get('fecha_termino', instance.fecha_termino)
        instance.vacantes = validated_data.get('vacantes',instance.vacantes)
        instance.cant_interesados = validated_data.get('cant_interesados', instance.cant_interesados)

        for habil in habilidades_datos:
            habil, created = Habilidad.objects.get_or_create(nombre=habil['nombre'])
            lista_habilidades.append(habil)

        instance.habilidad.set(lista_habilidades)
        instance.save()
        return instance



class SugerenciaSerializer(serializers.ModelSerializer):

    def create(self,validated_data):
        text=str(validated_data.get('detalle'))
        sugerencia = Sugerencia.objects.create(detalle=text)
        habilidades_datos = validated_data.pop('persona')
        person= Persona.objects.create(nombre=habilidades_datos['nombre'],apellido=habilidades_datos['apellido'],email=habilidades_datos['email'],telefono=habilidades_datos['telefono'],fecha_nacimiento=habilidades_datos['fecha_nacimiento'],lugar_origen=habilidades_datos['lugar_origen'])
        return sugerencia

    last_p = Persona.objects.last()
    last_s = Sugerencia.objects.last()
   # num=int(last_p.id)
   # iD=int(last_s.id)
  #  Sugerencia.objects.filter(id = iD).update(persona = num)

    persona=PersonaSerializer()
    class Meta:
        model=Sugerencia
        fields='__all__'


class NoticiaSerializer(serializers.ModelSerializer):
    administrador= AdministradorSerializer(read_only=True)
    class Meta:
        model=Noticia
        fields=['id','titulo','descripcion','administrador']
   