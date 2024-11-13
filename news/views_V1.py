from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post

def list_posts_v1(request):
    posts = Post.objects.all()
    return render(request, 'news/index.html', {'posts': posts})

def detail_post_v1(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/detail.html', {'post': post})

def create_post_v1(request):
    if request.method == 'POST':
        post = Post(
            titulo=request.POST.get('titulo'),
            conteudo=request.POST.get('conteudo'),
            img_url=request.POST.get('img_url')
        )
        post.save()
        return HttpResponseRedirect(reverse('news:list_v1'))
    return render(request, 'news/create.html')

def update_post_v1(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.titulo = request.POST.get('titulo')
        post.conteudo = request.POST.get('conteudo')
        post.img_url = request.POST.get('img_url')
        post.save()
        return HttpResponseRedirect(reverse('news:detail_v1', args=[pk]))
    return render(request, 'news/update.html', {'post': post})

def delete_post_v1(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse('news:list_v1'))
    return render(request, 'news/delete.html', {'post': post})
