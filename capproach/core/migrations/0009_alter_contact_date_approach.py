# Generated by Django 3.2.5 on 2021-08-01 18:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_date_apporach_contact_date_approach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_approach',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]