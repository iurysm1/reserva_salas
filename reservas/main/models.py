from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Sala(models.Model):
    numeroSalas = models.PositiveIntegerField()
    capacidade = models.PositiveIntegerField()



class Cadeira(models.Model):
    numeroCadeira=models.PositiveIntegerField(default=0)
    andar=models.CharField(max_length=1)
    status = models.BooleanField(default=False)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, null=True)