# Generated by Django 4.2.3 on 2023-08-01 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0002_customer_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='account_type',
        ),
    ]