import json
import os

from django.core.management.base import BaseCommand

from catalog.models import Category, Product
from config import settings


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        filepath = os.path.join(settings.BASE_DIR, 'catalog', 'fixture', 'category_data.json')
        if os.path.isfile(filepath):
            with open(filepath, encoding='utf-8') as file:
                data = json.load(file)
                return data

    @staticmethod
    def json_read_products():
        filepath = os.path.join(settings.BASE_DIR, 'catalog', 'fixture', 'product_data.json')
        if os.path.isfile(filepath):
            with open(filepath, encoding='utf-8') as file:
                data = json.load(file)
                return data

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_for_create = []
        product_for_create = []

        read_categories = Command.json_read_categories()
        if read_categories:
            for category in read_categories:
                category_for_create.append(Category(**category['fields']))
            Category.objects.bulk_create(category_for_create)

        read_products = Command.json_read_products()
        if read_products:
            for product in read_products:
                product_for_create.append(Product(**product['fields']))
            Product.objects.bulk_create(product_for_create)
