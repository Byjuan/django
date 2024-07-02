from django.db import models

# Create your models here.

class Usuarios(models.Model):

    nombre= models.CharField(max_length=40)
    pofesion=models.TextField()
    imagen_de_perfil=models.ImageField(upload_to="photos")
    ciudad=models.TextField()