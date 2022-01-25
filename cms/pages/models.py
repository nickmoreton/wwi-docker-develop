from django import forms
from django.db import models
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    ObjectList,
    StreamFieldPanel,
    TabbedInterface,
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail_wordpress_import.blocks import WPImportStreamBlocks
from wagtail_wordpress_import.models import WPImportedPageMixin


class PostPage(WPImportedPageMixin, Page):
    body = StreamField(WPImportStreamBlocks)
    categories = ParentalManyToManyField("pages.Category", blank=True)
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    author = models.ForeignKey(
        "pages.Author",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        SnippetChooserPanel("author"),
        ImageChooserPanel("header_image"),
        StreamFieldPanel("body"),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel("categories", widget=forms.CheckboxSelectMultiple),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(promote_panels, heading="Promote"),
            ObjectList(Page.settings_panels, heading="Settings", classname="settings"),
            ObjectList(WPImportedPageMixin.wordpress_panels, heading="Debug"),
        ]
    )

    def import_wordpress_data(self, data):
        # wagtail page model fields
        self.title = data["title"]
        self.slug = data["slug"]
        self.first_published_at = data["first_published_at"]
        self.last_published_at = data["last_published_at"]
        self.latest_revision_created_at = data["latest_revision_created_at"]
        self.search_description = data["search_description"]

        # debug fields
        self.wp_post_id = data["wp_post_id"]
        self.wp_post_type = data["wp_post_type"]
        self.wp_link = data["wp_link"]
        self.wp_raw_content = data["wp_raw_content"]
        self.wp_block_json = data["wp_block_json"]
        self.wp_processed_content = data["wp_processed_content"]
        self.wp_normalized_styles = data["wp_normalized_styles"]
        self.wp_post_meta = data["wp_post_meta"]

        # own model fields
        self.body = data["body"]


@register_snippet
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    panels = [FieldPanel("name")]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


@register_snippet
class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email_address = models.EmailField()

    panels = [
        FieldPanel("first_name"),
        FieldPanel("last_name"),
        FieldPanel("email_address"),
    ]

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"
