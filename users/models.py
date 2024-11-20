from django.db import models
from django.contrib.auth.models import User

class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100, default="")
    email = models.EmailField()
    cpf = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    crm = models.CharField(max_length=15)
    uf_crm = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.nome} - {self.crm}'

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=15)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome