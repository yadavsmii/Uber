# Generated by Django 4.2 on 2023-05-26 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_studentsaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='order_discounr',
            new_name='order_discount',
        ),
    ]