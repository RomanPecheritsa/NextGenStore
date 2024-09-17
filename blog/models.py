from django.db import models

from catalog.models import upload_to, BLANK_NULL_TRUE


class Article(models.Model):
    """
    Blog post model
    """
    title = models.CharField(max_length=100, verbose_name="заголовок")
    slug = models.SlugField(unique=True, verbose_name="slug", **BLANK_NULL_TRUE)
    content = models.TextField(verbose_name="cодержимое статьи")
    preview = models.ImageField(upload_to=upload_to, verbose_name="превью", **BLANK_NULL_TRUE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(default=True, verbose_name="опубликовано")
    views_count = models.IntegerField(default=0, verbose_name="просмотры")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('-created_at',)



