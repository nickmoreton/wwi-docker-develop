from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = "pages"

    # Un-commnet to use the import prefilters
    # def ready(self):
    #     from . import prefilters
