# Generated by Django 3.0.6 on 2020-06-22 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querymodels', '0002_auto_20200622_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
