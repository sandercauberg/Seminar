# Generated by Django 3.2.8 on 2021-10-28 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211028_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='endttime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='starttime',
            field=models.TimeField(null=True),
        ),
    ]