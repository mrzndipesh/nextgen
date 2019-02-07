# Generated by Django 2.1.5 on 2019-01-29 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20190129_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='productCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='store.Category'),
        ),
    ]