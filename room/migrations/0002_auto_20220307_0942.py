# Generated by Django 3.0 on 2022-03-07 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='room',
            new_name='rooms',
        ),
    ]