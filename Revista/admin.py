from django.contrib import admin

from .models import *

class AdminRevista(admin.TabularInline):
    model = revista
    extra = 1

class AdminColeçao(admin.ModelAdmin):
    inlines = [AdminRevista]

class AdminAmigo(admin.TabularInline):
    model = Amigo
    extra = 1

class AdminEmprestimo(admin.ModelAdmin):
    inlines = [AdminAmigo]
admin.site.register(revista)
admin.site.register(caixa)
admin.site.register(coleçao,AdminColeçao)
admin.site.register(emprestimo,AdminEmprestimo)
admin.site.register(Amigo)

# from django.contrib import admin
#
# from .models import *
#
# class RevistaInLine(admin.TabularInline):
#     model = Revista
#     extra = 1
#
# class AdminColecao(admin.ModelAdmin):
#     inlines = [RevistaInLine, ]
#
# class AmigoInLine(admin.TabularInline):
#     model = Amigo
#     extra = 1
#
# class AdminEmprestimo(admin.ModelAdmin):
#     inlines = [AmigoInLine, ]
#
# admin.site.register(Revista)
# admin.site.register(Caixa)
# admin.site.register(Colecao, AdminColecao)
# admin.site.register(Emprestimo, AdminEmprestimo)
# admin.site.register(Amigo)