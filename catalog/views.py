from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm
from catalog.models import Product, ContactInfo


class MainTemplateView(TemplateView):
    template_name = 'catalog/index.html'


class ContactTemplateView(TemplateView):
    template_name = "catalog/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_info"] = ContactInfo.objects.first()
        return context


class ProductListView(ListView):
    model = Product
    paginate_by = 6
    ordering = ["-created_at"]


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')



