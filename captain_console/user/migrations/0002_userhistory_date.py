# Generated by Django 3.0.5 on 2020-05-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userhistory',
            name='date',
            field=models.DateTimeField(default='2020-05-12 10:45:04'),
        ),
    ]
