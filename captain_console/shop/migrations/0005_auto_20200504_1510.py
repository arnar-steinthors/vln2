# Generated by Django 3.0.5 on 2020-05-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200504_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(default='static/images/no-image-found.png', max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.CharField(default='static/images/no-image-found.png', max_length=999),
        ),
    ]
