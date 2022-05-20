# Generated by Django 3.2.11 on 2022-01-24 21:40

try:
    import wagtail.blocks
except ImportError:
    from wagtail.core import blocks
try:
    import wagtail.fields
except ImportError:
    from wagtail.core import fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0008_add_email_to_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("rich_text", wagtail.blocks.RichTextBlock()),
                    (
                        "heading",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.blocks.CharBlock(form_classname="title"),
                                ),
                                (
                                    "importance",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("h1", "H1"),
                                            ("h2", "H2"),
                                            ("h3", "H3"),
                                            ("h4", "H4"),
                                            ("h5", "H5"),
                                            ("h6", "H6"),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "image",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "caption",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                ("link", wagtail.blocks.URLBlock(required=False)),
                                (
                                    "alignment",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("left", "Left"),
                                            ("right", "Right"),
                                            ("center", "Center"),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "block_quote",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "quote",
                                    wagtail.blocks.CharBlock(form_classname="title"),
                                ),
                                (
                                    "attribution",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    ("raw_html", wagtail.blocks.RawHTMLBlock()),
                ]
            ),
        ),
    ]
