import json
from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    """
    Custom management command to populate the database with data from a JSON fixture file.
    The command will first clear existing data from the Product and Category tables,
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

    def handle(self, *args, **options):
        """
        Main method that handles the execution of the command.

        - Deletes all existing data from the Product and Category tables.
        - Reads category and product data from the fixture file.
        - Creates new instances of Category and Product based on the fixture data.
        - Saves the new instances in bulk to the database.
        """
        # Clear existing data
        Product.objects.all().delete()
        Category.objects.all().delete()

        categories_for_create = []
        products_for_create = []

        for item in Command.json_read_categories():
            category_data = item["fields"]
            categories_for_create.append(Category(id=item["pk"], **category_data))

        Category.objects.bulk_create(categories_for_create)

        for item in Command.json_read_products():
            product_data = item["fields"]
            category = Category.objects.get(pk=product_data.pop("category"))
            products_for_create.append(
                Product(id=item["pk"], category=category, **product_data)
            )

        Product.objects.bulk_create(products_for_create)
        print("Success!")
