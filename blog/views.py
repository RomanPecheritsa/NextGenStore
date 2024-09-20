from django.urls import reverse_lazy
from pytils.translit import slugify
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)

from blog.models import Article
from blog.forms import ArticleUpdateForm


class ArticlesListView(ListView):
    model = Article
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleUpdateForm
    success_url = reverse_lazy("blog:article_list")

    def form_valid(self, form):
        if form.is_valid():
            item = form.save()
            item.slug = slugify(item.title)
            item.save()
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleUpdateForm

    def get_success_url(self):
        return reverse_lazy("blog:article_detail", kwargs={"pk": self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:article_list")
