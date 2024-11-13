from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'titulo',
            'conteudo',
            'img_url'
        ]
        labels = {
            'titulo': 'Título',
            'conteudo': 'Conteúdo',
            'img_url': 'URL da imagem',
        }