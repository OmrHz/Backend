# Generated by Django 5.0.10 on 2024-12-28 00:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Consultation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordonnance',
            fields=[
                ('IdOrdonnance', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('statue', models.CharField(choices=[('V', 'Validee'), ('NV', 'Non Validee'), ('A', 'Attente')], default='A', max_length=2)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultation_ordonnance', to='Consultation.consultation')),
            ],
        ),
    ]
