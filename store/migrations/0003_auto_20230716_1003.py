# Generated by Django 3.1 on 2023-07-16 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='variations_value',
            new_name='variation_value',
        ),
    ]
