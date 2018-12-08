from django.db import models
from django.contrib.auth.models import User


class Marca(models.Model):
	nome = models.CharField(max_length=100)
	sigle = models.CharField(max_length=3)
	def __str__(self):
		return self.nome

class Carro(models.Model):
	marca = models.ForeignKey(Marca, on_delete = models.CASCADE, related_name='carros')
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='meus_carros')
	modelo = models.CharField(max_length=100)
	ano_modelo = models.CharField(max_length=4)
	ano_fabricacao = models.CharField(max_length=4)
	nume_portas = models.IntegerField(default=2)
	#descricao = models.TextField()
	foto = models.ImageField(null=True, blank=True, upload_to = 'media/')
	def __str__(self):
		return self.modelo

class Acessorio(models.Model):
	nome = models.CharField(max_length=256)
	carro = models.ManyToManyField(Carro)
	def __str__(self):
		return self.nome