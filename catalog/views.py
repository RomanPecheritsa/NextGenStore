from django.shortcuts import render
from catalog.models import Product, ContactInfo


def home(request):
    last_products = Product.objects.order_by("-created_at")[:6]
    for item in last_products:
        print(f"{item.name} | {item.description} | {item.price}$")
    return render(request, "catalog/home.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print(f"{name} ({email}): {message}")

    contact_info = ContactInfo.objects.first()

    return render(request, "catalog/contact.html", {"contact_info": contact_info})
