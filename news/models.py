from django.db import models
from django.conf import settings

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    img_url = models.URLField(max_length=255, null=True)
    data_postagem = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.titulo 