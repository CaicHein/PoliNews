from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm

def list_posts_v2(request):
    posts = Post.objects.all()
    return render(request, 'news/index.html', {'posts': posts})

def detail_post_v2(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/detail.html', {'post': post})

def create_post_v2(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('news:list_v2'))
    else:
        form = PostForm()
    return render(request, 'news/create.html', {'form': form})

def update_post_v2(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('news:detail_v2', args=[pk]))
    else:
        form = PostForm(instance=post)
    return render(request, 'news/update.html', {'form': form})

def delete_post_v2(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse('news:list_v2'))
    return render(request, 'news/delete.html', {'post': post})
