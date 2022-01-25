# Generated by Django 3.2.11 on 2022-01-24 21:40

import wagtail.core.blocks
import wagtail.core.fields
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
            field=wagtail.core.fields.StreamField(
                [
                    ("rich_text", wagtail.core.blocks.RichTextBlock()),
                    (
                        "heading",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.core.blocks.CharBlock(
                                        form_classname="title"
                                    ),
                                ),
                                (
                                    "importance",
                                    wagtail.core.blocks.ChoiceBlock(
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
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "caption",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                ("link", wagtail.core.blocks.URLBlock(required=False)),
                                (
                                    "alignment",
                                    wagtail.core.blocks.ChoiceBlock(
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
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "quote",
                                    wagtail.core.blocks.CharBlock(
                                        form_classname="title"
                                    ),
                                ),
                                (
                                    "attribution",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    ("raw_html", wagtail.core.blocks.RawHTMLBlock()),
                ]
            ),
        ),
    ]