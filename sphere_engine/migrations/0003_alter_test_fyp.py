# Generated by Django 3.2 on 2021-11-23 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0005_alter_fyp_team_members'),
        ('sphere_engine', '0002_rename_event_date_test_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='fyp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='fyp.fyp'),
        ),
    ]