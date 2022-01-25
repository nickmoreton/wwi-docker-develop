from django.core.management.base import BaseCommand
from wagtail.documents.models import Document


class Command(BaseCommand):
    def handle(self, *args, **options):
        Document.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Successfully deleted all documents"))
