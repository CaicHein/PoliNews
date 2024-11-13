from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post
from .forms import PostForm

class ListView(generic.ListView):
    model = Post
    template_name = 'news/index.html'

class DetailView(generic.DetailView):
    model = Post
    template_name = 'news/detail.html'

class CreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/create.html'
    permission_required = 'news.add_post'

class UpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/update.html'
    permission_required = 'news.change_post'

class DeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'news/delete.html'
    success_url = reverse_lazy('news:index')
    permission_required = 'news.delete_post'

