# Generated by Django 3.0.3 on 2020-05-12 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200512_1435'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerimages',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]
