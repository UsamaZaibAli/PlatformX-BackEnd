# Generated by Django 3.2 on 2021-08-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_alter_workshop_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]