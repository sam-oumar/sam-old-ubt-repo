# Generated by Django 3.0.6 on 2020-11-21 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clbaseviews', '0017_auto_20201121_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
