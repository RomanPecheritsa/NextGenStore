from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticlesListView, ArticleDetailView


app_name = BlogConfig.name

urlpatterns = [
    path("", ArticlesListView.as_view(), name="article_list"),
    path("view/<int:pk>", ArticleDetailView.as_view(), name="article_detail"),
    # path("create/", ..., name="create_article"),
    # path("edit/<int:pk>", ..., name="update_article"),
    # path("delete/<int:pk>/", ..., name="delete_article")
]
