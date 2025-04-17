# Generated by Django 5.1.7 on 2025-04-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_remove_tariff_end_date_remove_tariff_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='status',
            field=models.CharField(choices=[('unpaid', 'unpaid'), ('paid', 'unpaid'), ('overdue', 'overdue')], default='unpaid', max_length=50),
        ),
    ]
