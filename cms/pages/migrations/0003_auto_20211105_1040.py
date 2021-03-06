# Generated by Django 3.2.7 on 2021-11-05 10:40

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_auto_20211025_1530"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="postpage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "rich_text",
                        wagtail.core.blocks.RichTextBlock(
                            features=[
                                "anchor-identifier",
                                "h1",
                                "h2",
                                "h3",
                                "h4",
                                "h5",
                                "h6",
                                "bold",
                                "italic",
                                "ol",
                                "ul",
                                "hr",
                                "link",
                                "document-link",
                                "image",
                                "embed",
                                "superscript",
                                "subscript",
                                "strikethrough",
                                "blockquote",
                            ]
                        ),
                    ),
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
