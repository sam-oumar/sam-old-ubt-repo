# Generated by Django 3.0.6 on 2020-06-01 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clbaseviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='none',
            new_name='number',
        ),
    ]
