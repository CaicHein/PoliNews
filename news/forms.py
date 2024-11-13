from django.forms import ModelForm
from .models import Post, Comment
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'img_url', 'categorias']
        labels = {
            'titulo': 'Título',
            'conteudo': 'Conteúdo',
            'img_url': 'URL da imagem',
            'categorias': 'Categorias',
        }
    
    def clean_categorias(self):
        categorias = self.cleaned_data.get('categorias')
        if not categorias:
            raise forms.ValidationError("É necessário selecionar ao menos uma categoria.")
        return categorias

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['texto']
        labels = {
            'texto': 'Comentário',
        }