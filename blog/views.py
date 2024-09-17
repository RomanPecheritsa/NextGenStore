from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Article


class ArticlesListView(ListView):
    model = Article
    paginate_by = 10


class ArticleDetailView(DetailView):
    model = Article


