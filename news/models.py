from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    img_url = models.URLField(max_length=255, null=True)
    data_postagem = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.titulo 
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    data_postagem = models.DateTimeField(default=timezone.now) 

    class Meta:
        ordering = ['-data_postagem']

    def __str__(self):
        return f'"{self.texto}" - {self.autor.username}'