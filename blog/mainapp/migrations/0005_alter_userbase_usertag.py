# Generated by Django 4.1.7 on 2023-05-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_userbase_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='usertag',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
