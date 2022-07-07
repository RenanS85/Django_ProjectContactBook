from codecs import charmap_build
from hashlib import blake2b
import imp
from django.db import models
from django.utils import timezone
'''
CONTATOS
id: INT (automático)
nome: STR * (obrigatório)
sobrenome: STR (opcional)
telefone: STR * (obrigatório)
email: STR (opcional)
data_criacao: DATETIME (automático)
descricao: texto
categoria: CATEGORIA (outro model)

 CATEGORIA
 id: INT
 nome: STR * (obrigatório)

'''

class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155, blank=True)
    phone = models.CharField(max_length=155)
    email = models.CharField(max_length=155)
    create_date = models.DateTimeField(default=timezone.now())
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete= models.DO_NOTHING)
    show = models.BooleanField(default=True)
    photo = models.ImageField(blank = True, upload_to = 'photos/%Y/%m/%d')

    def __str__(self):
        return self.name

