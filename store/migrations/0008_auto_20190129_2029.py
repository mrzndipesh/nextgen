# Generated by Django 2.1.5 on 2019-01-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_sliderimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='image',
            field=models.ImageField(upload_to='store/static/slider/img'),
        ),
    ]
