from django.db import models

class coleçao(models.Model):
    nome = models.CharField(max_length=20)


class caixa(models.Model):
    numero = models.IntegerField()
    etiqueta = models.CharField(max_length=20)
    cor = models.CharField(max_length=15)

class emprestimo(models.Model):
    data_emprestimo = models.DateField()
    data_devoluçao = models.DateField()

class revista(models.Model):
    numero_ediçao = models.IntegerField()
    ano = models.IntegerField()
    coleçao = models.ForeignKey(coleçao, on_delete=models.CASCADE)
    caixa = models.ForeignKey(caixa, on_delete=models.CASCADE)
    emprestimo = models.ForeignKey(emprestimo, on_delete=models.CASCADE)

grupo = (('1','Predio'),('2','Escola'))
class Amigo(models.Model):
    nome = models.CharField(max_length=100)
    nome_da_mae = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    grupo_amigo = models.CharField(max_length=100,choices=grupo)
    emprestimo = models.ForeignKey(emprestimo, on_delete=models.CASCADE)

# from django.db import models
#
# tupla = (('E', 'Escola'),('P','Prédio'))
#
# class Colecao(models.Model):
#     nome = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.nome
#
#
# class Caixa(models.Model):
#     numero = models.IntegerField()
#     etiqueta = models.CharField(max_length=100)
#     cor = models.CharField(max_length=50)
#
#
# class Revista(models.Model):
#     numero_edicao = models.IntegerField()
#     ano = models.IntegerField()
#     colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE)
#     caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)
#
#
# class Amigo(models.Model):
#     nome = models.CharField(max_length=100)
#     nome_mae = models.CharField(max_length=100)
#     telefone = models.CharField(max_length=20)
#     grupo_amigo = models.CharField(max_length=100, choices=tupla)
#     revista = models.ManyToManyField(Revista, through='Emprestimo')
#
#     def __str__(self):
#         return self.nome
#
#
# class Emprestimo(models.Model):
#     revista = models.ForeignKey(Revista, on_delete=models.CASCADE)
#     amigo = models.ForeignKey(Amigo, on_delete=models.CASCADE)
#     data_emprestimo = models.DateField(auto_now_add=True)
#     data_devolucao = models.DateField()
#
