# Generated by Django 4.1.7 on 2023-05-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
