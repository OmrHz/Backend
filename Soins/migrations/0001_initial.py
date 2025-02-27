# Generated by Django 5.0.10 on 2024-12-28 00:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DPI', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Soin',
            fields=[
                ('IdSoin', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('soins', models.CharField(max_length=255)),
                ('observations', models.TextField(blank=True, default='', null=True)),
                ('DPI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DPI_Soin', to='DPI.dpi')),
                ('infermier', models.ForeignKey(limit_choices_to={'role': 'infermier'}, on_delete=django.db.models.deletion.CASCADE, related_name='Soin_infermier', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
