# Generated by Django 4.2.3 on 2023-08-02 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0006_delete_material_remove_userinfo_account_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reginfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=25)),
                ('cpass', models.CharField(max_length=25)),
            ],
        ),
    ]
