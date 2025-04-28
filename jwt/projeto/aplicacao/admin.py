# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioDS16

class UsuarioDS16Admin(UserAdmin):
    # O que irá aparecer na tela 
    list_display= ('username', 'biografia', 'idade', 'telefone', 'endereco',  'escolaridade', 'quant_animal') 

    fieldsets= UserAdmin.fieldsets +(
        (None, {'fields': ('biografia', 'idade', 'telefone','endereco',  'escolaridade', 'quant_animal')}),
    )

    add_fieldsets= UserAdmin.add_fieldsets +(
        (None, {'fields': ('biografia', 'idade', 'telefone','endereco', 'escolaridade', 'quant_animal')}),
    )

admin.site.register(UsuarioDS16, UsuarioDS16Admin)
