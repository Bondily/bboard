# Generated by Django 2.0.13 on 2019-05-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20190426_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='kind',
            field=models.CharField(blank=True, choices=[('b', 'Куплю'), ('c', 'Обменяю'), (None, 'Выберите действие'), ('s', 'Продам')], max_length=1),
        ),
    ]
