import json
from django.core.management.base import BaseCommand
from catalog.models import Product, Category, ContactInfo


class Command(BaseCommand):
    """
    Custom management command to populate the database with data from a JSON fixture file.
    The command will first clear existing data from the Product, Category, and ContactInfo tables,
    and then repopulate them with the data from the fixture file `catalog_data.json`.
    """

    @staticmethod
    def json_read_categories():
        """
        Reads and filters category data from the fixture file.

        Returns:
            list: A list of dictionaries containing data for Category model instances.
        """
        with open("fixtures/catalog_data.json", encoding="utf-8") as file:
            data = json.load(file)
            return [item for item in data if item["model"] == "catalog.category"]

    @staticmethod
    def json_read_products():
        """
        Reads and filters product data from the fixture file.

        Returns:
            list: A list of dictionaries containing data for Product model instances.
        """
        with open("fixtures/catalog_data.json", encoding="utf-8") as file:
            data = json.load(file)
            return [item for item in data if item["model"] == "catalog.product"]

    @staticmethod
    def json_read_contact_info():
        """
        Reads and filters contact information data from the fixture file.

        Returns:
            list: A list of dictionaries containing data for ContactInfo model instances.
        """
        with open("fixtures/catalog_data.json", encoding="utf-8") as file:
            data = json.load(file)
            return [item for item in data if item["model"] == "catalog.contactinfo"]

    def handle(self, *args, **options):
        """
        Main method that handles the execution of the command.

        - Deletes all existing data from the Product, Category, and ContactInfo tables.
        - Reads category, product, and contact information data from the fixture file.
        - Creates new instances of Category, Product, and ContactInfo based on the fixture data.
        - Saves the new instances in bulk to the database.
        """
        Product.objects.all().delete()
        Category.objects.all().delete()
        ContactInfo.objects.all().delete()

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

        print("Success!")
