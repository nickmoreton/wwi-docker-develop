# Generated by Django 3.2.7 on 2021-11-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0007_postpage_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="email_address",
            field=models.EmailField(default="admin@example.com", max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="author",
            name="first_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="author",
            name="last_name",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
