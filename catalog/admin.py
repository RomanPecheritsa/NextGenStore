from django.contrib import admin

from catalog.models import Category, Product, ContactInfo
from blog.models import Article


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("price", "name", "category")
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("phone", "email", "address")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "created_at", "is_published", "slug")
    list_filter = ("created_at", "is_published")
    search_fields = ("title", "content")