from django.urls import path
from catalog.views import contact, home
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name


urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
]
