# Generated by Django 5.1.1 on 2024-10-15 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0006_alter_diagnosis_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='approved',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]