# Generated by Django 5.0.10 on 2024-12-29 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicaments', '0001_initial'),
        ('Ordonnance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamentordonnance',
            name='Medicament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicament_ordonnance', to='Medicaments.medicament'),
        ),
        migrations.AlterField(
            model_name='medicamentordonnance',
            name='Ordonnance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordonnance_medicament', to='Ordonnance.ordonnance'),
        ),
    ]
