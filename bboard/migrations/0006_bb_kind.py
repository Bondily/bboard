# Generated by Django 2.0.13 on 2019-05-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0005_remove_bb_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='kind',
            field=models.CharField(blank=True, choices=[('b', 'Куплю'), ('s', 'Продам'), ('c', 'Обменяю')], max_length=1),
        ),
    ]
