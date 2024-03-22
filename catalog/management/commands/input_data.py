import json
import os

from django.core.management.base import BaseCommand

from catalog.models import Category, Product, Contact
from config import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.clear_data()
        self.import_data(Category, 'category_data.json')
        self.import_data(Product, 'product_data.json')
        self.import_data(Contact, 'contact_data.json')

    @staticmethod
    def clear_data():
        Category.objects.all().delete()
        Product.objects.all().delete()
        Contact.objects.all().delete()

    @staticmethod
    def import_data(model, filename):
        data = Command.read_data(filename)
        objects_to_create = []
        if data:
            for item in data:
                objects_to_create.append(model(**item['fields']))
            model.objects.bulk_create(objects_to_create)

    @staticmethod
    def read_data(filename):
        filepath = os.path.join(settings.BASE_DIR, 'catalog', 'fixture', filename)
        if os.path.isfile(filepath):
            with open(filepath, encoding='utf-8') as file:
                data = json.load(file)
                return data
