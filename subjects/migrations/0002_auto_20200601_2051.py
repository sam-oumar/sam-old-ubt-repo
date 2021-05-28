# Generated by Django 3.0.5 on 2020-06-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['-year']},
        ),
        migrations.AlterField(
            model_name='subject',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='subjectimage',
            name='image_file',
            field=models.ImageField(default='default.png', upload_to='subject_img'),
        ),
    ]
