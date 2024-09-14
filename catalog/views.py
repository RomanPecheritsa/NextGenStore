from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from catalog.models import Product, ContactInfo


def home(request):
    product_list = Product.objects.all().order_by("-created_at")
    paginator = Paginator(product_list, 6)

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context = {"products": product_list, "page_obj": page_obj}
    return render(request, "catalog/index.html", context)


def contact(request):
    contacts = ContactInfo.objects.first()
    context = {
        "contact_info": contacts,
    }
    return render(request, "catalog/contact.html", context)


def product(request, pk):
    item = get_object_or_404(Product, pk=pk)
    context = {"product": item}
    return render(request, "catalog/product_detail.html", context)
