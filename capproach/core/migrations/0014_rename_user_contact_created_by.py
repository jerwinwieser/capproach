# Generated by Django 3.2.5 on 2021-08-01 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_contact_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user',
            new_name='created_by',
        ),
    ]
