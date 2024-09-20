from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import Product, ContactInfo


class ProductListView(ListView):
    model = Product
    paginate_by = 6
    ordering = ["-created_at"]


class ContactTemplateView(TemplateView):
    template_name = "catalog/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_info"] = ContactInfo.objects.first()
        return context


class ProductDetailView(DetailView):
    model = Product
