# Generated by Django 3.2 on 2021-12-13 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0009_auto_20211213_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='join_url',
            field=models.TextField(default=''),
        ),
    ]
