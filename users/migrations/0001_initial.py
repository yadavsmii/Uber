# Generated by Django 4.2 on 2023-05-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=15, null=True)),
                ('surname', models.CharField(blank=True, max_length=15, null=True)),
                ('birth', models.DateField(blank=True, max_length=10, null=True)),
                ('mobile_number', models.IntegerField(blank=True, max_length=10, null=True)),
                ('gender_type', models.IntegerField(choices=[(1, 'Female'), (2, 'Male'), (3, 'Others')])),
            ],
        ),
    ]
