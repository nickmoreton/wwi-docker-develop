from django.core.management.base import BaseCommand
from wagtail.images.models import Image


class Command(BaseCommand):
    def handle(self, *args, **options):
        Image.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Successfully deleted all images"))
