# Generated by Django 3.2.8 on 2021-10-28 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211028_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='endttime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='starttime',
            field=models.DateTimeField(null=True),
        ),
    ]
