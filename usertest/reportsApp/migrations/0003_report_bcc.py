# Generated by Django 5.1 on 2024-08-12 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsApp', '0002_alter_report_cc_alter_report_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='bcc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
