from django.core.cache import cache

from catalog.models import Category
from nextgenstore.settings import CACHES_ENABLE


def get_categories_from_cache():
    if not CACHES_ENABLE:
        return Category.objects.all()

    key = f'categories_list'
    categories = cache.get(key)

    if categories is None:
        categories = Category.objects.all()
        cache.set(key, categories)

    return categories