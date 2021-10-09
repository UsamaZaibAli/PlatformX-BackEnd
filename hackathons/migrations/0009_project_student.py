# Generated by Django 3.2 on 2021-10-08 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20211005_0448'),
        ('hackathons', '0008_auto_20211009_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='student',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='project', to='user.student'),
        ),
    ]