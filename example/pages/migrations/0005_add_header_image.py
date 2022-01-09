# Generated by Django 3.2.7 on 2021-11-16 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('pages', '0004_postpage_wp_post_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpage',
            name='header_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.image'),
        ),
    ]
