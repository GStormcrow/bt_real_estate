# Generated by Django 5.1.2 on 2025-01-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_remove_listing_lot_size_listing_loft_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=6),
        ),
    ]
