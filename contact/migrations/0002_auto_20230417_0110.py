# Generated by Django 3.2 on 2023-04-17 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='street_address1',
            new_name='street_address',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='contact_option',
            new_name='subject',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='street_address2',
        ),
    ]