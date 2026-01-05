from django.db import models

class Tarefas(models.Model):
    nome = models.CharField(max_length=100)
    feita = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

# Create your models here.
