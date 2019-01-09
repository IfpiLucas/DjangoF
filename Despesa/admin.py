from django.contrib import admin

from .models import *


class AdminDespesas(admin.ModelAdmin):
    list_display = ('data_criaçao', 'tipo_despesa', 'forma_pagamento', 'descriçao', 'vencimento', 'quitado','Dias_Para_Vencimento')
    list_filter = ('quitado', 'vencimento')

admin.site.register(Despesa, AdminDespesas)
