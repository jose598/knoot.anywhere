from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Anuncio,Habilidad,Categoria,Facultad,Persona,Consumidor,Administrador,Noticia,User

admin.site.register(Anuncio)
admin.site.register(Categoria)
admin.site.register(Habilidad)
admin.site.register(Facultad)
admin.site.register(Persona)
admin.site.register(Consumidor)
admin.site.register(Administrador)
admin.site.register(Noticia)

class Account(UserAdmin):
    list_display= ('email','username','fecha','fecha_log','is_admin','is_staff')
    search_fields=('email','username')
    readonly_fields=('fecha','fecha_log')

    filter_horizontal=()
    list_filter=()
    fieldsets=()


admin.site.register(User,Account)