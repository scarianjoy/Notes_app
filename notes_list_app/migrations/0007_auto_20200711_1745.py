# Generated by Django 3.0.7 on 2020-07-11 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_list_app', '0006_auto_20200711_1737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='title',
            new_name='heading',
        ),
    ]
