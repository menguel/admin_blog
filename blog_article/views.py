from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Artblog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .form import ArticleForm

# Create your views here.


class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'blog/article_create.html'
    queryset = Artblog.objects.all()
    success_url = '/blog_article'

    def form_valid(self, form) :
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    form_class = ArticleForm
    template_name = 'blog/article_create.html'
    queryset = Artblog.objects.all()

    success_url = '/blog_article'
    


class ArticleLisView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Artblog.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    queryset = Artblog.objects.all()

    # Apres avoir écrit cette methode queryset n'aide plus en rien

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Artblog, pk=id_ )
    
class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    queryset = Artblog.objects.all()

    success_url = '/blog_article'

    #ou
    
