# Generated by Django 3.2.8 on 2021-10-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='dates',
            field=models.DateTimeField(),
        ),
    ]
