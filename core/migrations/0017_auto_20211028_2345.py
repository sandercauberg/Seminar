# Generated by Django 3.2.8 on 2021-10-28 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20211028_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='endtime',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='date',
            name='starttime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='dates',
            field=models.DateField(null=True),
        ),
    ]