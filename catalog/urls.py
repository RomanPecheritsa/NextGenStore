from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (
    ProductListView,
    ContactTemplateView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    MainTemplateView,
    ProductDeleteView,
)
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path("", MainTemplateView.as_view(), name="home"),
    path("contact/", ContactTemplateView.as_view(), name="contact"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/edit/<int:pk>/", ProductUpdateView.as_view(), name="product_edit"),
    path("products/delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
]
