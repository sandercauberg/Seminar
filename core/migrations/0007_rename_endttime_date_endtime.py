# Generated by Django 3.2.8 on 2021-10-28 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20211028_2251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date',
            old_name='endttime',
            new_name='endtime',
        ),
    ]