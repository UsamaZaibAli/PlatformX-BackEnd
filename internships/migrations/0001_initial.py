# Generated by Django 3.2 on 2021-11-25 12:47

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0011_auto_20211005_0448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None)),
                ('responsibilities', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None)),
                ('duration', models.IntegerField()),
                ('working_hour', models.IntegerField()),
                ('is_certificate', models.BooleanField()),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('stipend', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internship', to='user.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='internship_participant', serialize=False, to='user.student')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('internship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant', to='internships.internship')),
            ],
        ),
    ]
