from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import AnuncioViewSet,CategoriaViewSet,HabilidadViewSet,FacultadViewSet,PersonaViewSet,ConsumidorViewSet,SugerenciaViewSet,NoticiaViewSet,UserViewSet

router = DefaultRouter()
router.register(r'Anuncios',AnuncioViewSet)
router.register(r'Categorias',CategoriaViewSet)
router.register(r'Habilidades',HabilidadViewSet)
router.register(r'Facultades',FacultadViewSet)
router.register(r'Personas',PersonaViewSet)
router.register(r'Consumidores',ConsumidorViewSet)
router.register(r'Sugerencias',SugerenciaViewSet)
router.register(r'Noticias',NoticiaViewSet)
router.register(r'Usuarios',UserViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path(r'credenciales/',include('rest_auth.urls')),
    path(r'credenciales/registration',include('rest_auth.registration.urls')),
]
