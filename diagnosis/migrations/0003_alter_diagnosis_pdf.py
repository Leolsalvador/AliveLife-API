# Generated by Django 5.1 on 2024-09-01 23:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0002_diagnosis_pdf'),
        ('pdf', '0004_alter_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='pdf',
            field=models.ForeignKey(default='5', on_delete=django.db.models.deletion.CASCADE, to='pdf.pdf'),
        ),
    ]
