# Generated by Django 3.2.5 on 2021-08-08 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='time_approach',
        ),
    ]
