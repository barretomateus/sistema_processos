from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    matricula = models.CharField(unique=True, max_length=9)

    USERNAME_FIELD = 'matricula'


class UserData(models.Model):
    nome = models.CharField(max_length=255)
    doc_identificacao = models.CharField(max_length=12)
    doc_tipo = models.CharField(max_length=40)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=40)
    telefone = models.CharField(max_length=15)
    cep = models.CharField(max_length=9, blank=False, null=False)
    curso = models.CharField(max_length=100)

    aluno = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome + ', ' + self.doc_identificacao + ', ' + self.curso


class Processo(models.Model):
    numero = models.CharField(max_length=18, blank=True)
    tipo_processo = models.TextField(blank=False)
    esclarecimentos = models.TextField(blank=False)
    natureza_processo = models.CharField(max_length=100)
    parecer = models.CharField(max_length=40)

    user_data = models.ForeignKey(
        UserData,
        on_delete=models.SET_NULL,
        null=True
    )

    aluno = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
