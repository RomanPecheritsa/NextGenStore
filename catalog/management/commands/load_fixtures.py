import json
from django.core.management.base import BaseCommand
from catalog.models import Product, Category, ContactInfo
from blog.models import Article

PATH = "fixtures/load_data.json"


class Command(BaseCommand):
    """
    Custom management command to populate the database with data from a JSON fixture file.
    The command will first clear existing data from the Product, Category, ContactInfo, and Article tables,
    and then repopulate them with the data from the fixture file `catalog_data.json`.
    """

    @staticmethod
    def json_read_categories():
        with open(PATH, encoding="utf-8") as file:
            data = json.load(file)
            return [item for item in data if item["model"] == "catalog.category"]

    @staticmethod
    def json_read_products():
        with open(PATH, encoding="utf-8") as file:
            data = json.load(file)
            return [item for item in data if item["model"] == "catalog.product"]

    @staticmethod
    def json_read_contact_info():
        with open(PATH, encoding="utf-8") as file:
            data = json.load(file)
            return [item for item in data if item["model"] == "catalog.contactinfo"]

    @staticmethod
    def json_read_articles():
        with open(PATH, encoding="utf-8") as file:
            data = json.load(file)
            return [item for item in data if item["model"] == "blog.article"]

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        ContactInfo.objects.all().delete()
        Article.objects.all().delete()

        categories_for_create = []
        for item in Command.json_read_categories():
            category_data = item["fields"]
            categories_for_create.append(Category(id=item["pk"], **category_data))
        Category.objects.bulk_create(categories_for_create)

        products_for_create = []
        for item in Command.json_read_products():
            product_data = item["fields"]
            category = Category.objects.get(pk=product_data.pop("category"))
            products_for_create.append(
                Product(id=item["pk"], category=category, **product_data)
            )
        Product.objects.bulk_create(products_for_create)

        contact_info_for_create = []
        for item in Command.json_read_contact_info():
            contact_data = item["fields"]
            contact_info_for_create.append(ContactInfo(id=item["pk"], **contact_data))
        ContactInfo.objects.bulk_create(contact_info_for_create)

        articles_for_create = []
        for item in Command.json_read_articles():
            article_data = item["fields"]
            articles_for_create.append(Article(id=item["pk"], **article_data))
        Article.objects.bulk_create(articles_for_create)

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена'))
