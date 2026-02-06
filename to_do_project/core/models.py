from django.db import models

# Create your models here.
class Tarefa(models.Model):
    tarefaText = models.CharField(255)
    dificuldade = models.CharField(255)
    dataConclusao = models.DateField()
    dataCriacao = models.DateField(auto_now=True)