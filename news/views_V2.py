from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment
from .forms import PostForm, CommentForm

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

def create_comment_v2(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.autor = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('news:detail', args=(post_id, )))
    else:
        form = CommentForm()
    
    context = {'form': form, 'post': post}
    return render(request, 'news/comment.html', context)
