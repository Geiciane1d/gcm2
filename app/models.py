from django.db import models

class Aluno(models.Model):
    nome=models.CharField(max_length=50)
    endereco=models.CharField(max_length=70)

    def __str__(self):
        return self.nome
