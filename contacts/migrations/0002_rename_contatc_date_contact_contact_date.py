# Generated by Django 5.1.2 on 2025-02-20 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contatc_date',
            new_name='contact_date',
        ),
    ]
