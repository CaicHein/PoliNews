from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import get_object_or_404

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
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        return super().form_valid(form)

class UpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/update.html'
    permission_required = 'news.change_post'
    success_url = reverse_lazy('news:index')

class DeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'news/delete.html'
    success_url = reverse_lazy('news:index')
    permission_required = 'news.delete_post'

class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'news/comment.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('news:detail', args=(self.kwargs['id'], ))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['id'])
        return context
    
