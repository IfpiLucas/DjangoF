from django.contrib import admin
from .models import *

class TurmaInLine(admin.TabularInline):
    model = Turma
    extra = 1

class AdminProfessor(admin.ModelAdmin):
    inlines = [TurmaInLine, ]

class AdminTurma(admin.ModelAdmin):
    list_display = ('chave', 'chave1', 'data_inicio', 'data_termino')

admin.site.register(Curso)
admin.site.register(Turma, AdminTurma)
admin.site.register(Professor, AdminProfessor)