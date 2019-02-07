# Generated by Django 2.1.5 on 2019-01-28 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productCategory',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
