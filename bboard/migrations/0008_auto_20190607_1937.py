# Generated by Django 2.0.13 on 2019-06-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0007_auto_20190522_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='content',
            field=models.TextField(blank=True, null=True, unique=True, verbose_name='Описание'),
        ),
    ]
