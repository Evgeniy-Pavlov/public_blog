# Generated by Django 4.1.7 on 2023-05-23 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_news_imagesnews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesnews',
            options={'verbose_name_plural': 'ImagesNews'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
    ]
