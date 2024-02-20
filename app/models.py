from django.db import models

class Customer(models.Model):
    nome = models.CharField(max_length=100)    
    limite = models.IntegerField(null=True, default=0)
    saldo = models.IntegerField(null=True, default=0)


class Transaction(models.Model):
    valor = models.IntegerField()
    tipo = models.CharField(max_length=1)
    descricao = models.CharField(max_length=10, default="descricao")
    realizada_em = models.DateTimeField()
    status = models.CharField(max_length=10, default='ERRO')
    cliente = models.ForeignKey(Customer, on_delete=models.CASCADE)
