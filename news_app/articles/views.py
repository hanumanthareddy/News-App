from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class EditArticle(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'edit_article.html'
    fields = ('title', 'body', )
    login_url = 'login'
    success_url = reverse_lazy('articles_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CreateArticle(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'create_article.html'
    fields = ('title', 'body', )
    login_url = 'login'
    success_url = reverse_lazy('articles_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteArticle(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'delete_article.html'
    login_url = 'login'
    success_url = reverse_lazy('articles_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DetailedArticle(DetailView):
    model = Article
    template_name = 'article_details.html'

