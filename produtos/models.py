

from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    qtd = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome
