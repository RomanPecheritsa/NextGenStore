from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from decimal import Decimal
import os

BLANK_NULL_TRUE = {"blank": True, "null": True}


def upload_to(instance, filename):
    """
    Generate a file upload path based on the model type.

    Args:
        instance (models.Model): The model instance for which the file is being uploaded.
        filename (str): The name of the file being uploaded.

    Returns:
        str: The path where the file will be saved, in the format 'uploads/<model_name>/<filename>'.

    Example:
        If the model is `Product` and the file name is `image.jpg`, the path will be `uploads/product/image.jpg`.
    """
    return f"uploads/{instance.__class__.__name__.lower()}/{filename}"


class Category(models.Model):
    """
    A model for storing product categories.
    """

    name = models.CharField(max_length=50, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    """
    A model for storing information about products.
    """

    name = models.CharField(max_length=50, verbose_name="Наименование товара")
    description = models.TextField(**BLANK_NULL_TRUE, verbose_name="Описание товара")
    preview = models.ImageField(
        **BLANK_NULL_TRUE, upload_to=upload_to, verbose_name="Изображение товара"
    )
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        verbose_name="Цена за покупку",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "-price", "created_at", "-updated_at"]


class ContactInfo(models.Model):
    """
    Model to store static contact information.
    """

    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Почта")
    address = models.TextField(verbose_name="Адрес")

    def __str__(self):
        return f"{self.phone}" f"{self.email}" f"{self.address}"

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактные информации"


@receiver(post_delete, sender=Product)
def delete_image(sender, instance, **kwargs):
    """
    Delete the file from filesystem when the corresponding `Product` object is deleted.

    Args:
        sender (Type[models.Model]): The model class that sent the signal.
        instance (Product): The instance of the model that is being deleted.
    """
    if instance.preview:
        if os.path.isfile(instance.preview.path):
            os.remove(instance.preview.path)
