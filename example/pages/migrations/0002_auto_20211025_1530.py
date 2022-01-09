# Generated by Django 3.2.7 on 2021-10-25 15:30

from django.db import migrations, models
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.RemoveField(
            model_name='pagepage',
            name='page_ptr',
        ),
        migrations.AddField(
            model_name='postpage',
            name='wp_block_json',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postpage',
            name='wp_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postpage',
            name='wp_normalized_styles',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postpage',
            name='wp_processed_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postpage',
            name='wp_raw_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='postpage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(features=['anchor-identifier', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'superscript', 'subscript', 'strikethrough', 'blockquote'])), ('heading', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(form_classname='title')), ('importance', wagtail.core.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')]))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(form_classname='title')), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock())]),
        ),
        migrations.DeleteModel(
            name='NewsPage',
        ),
        migrations.DeleteModel(
            name='PagePage',
        ),
        migrations.AddField(
            model_name='postpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='pages.Category'),
        ),
    ]
