# Generated by Django 2.1.4 on 2019-01-09 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criaçao', models.DateField()),
                ('tipo_despesa', models.CharField(choices=[('roupa', 'Roupa'), ('remedio', 'Remedio'), ('Alimentaçao', 'Alimentaçao'), ('1', 'Educaçao'), ('2', 'Transporte')], max_length=40)),
                ('descriçao', models.CharField(max_length=100)),
                ('forma_pagamento', models.CharField(choices=[('1', 'Dinheiro'), ('2', 'Cartao de Credito'), ('3', 'Cartao de debito')], max_length=100)),
                ('vencimento', models.DateField()),
                ('quitado', models.BooleanField()),
            ],
        ),
    ]
