# Generated by Django 3.2.8 on 2021-10-28 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_seminar_dates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='endtime',
        ),
        migrations.RemoveField(
            model_name='date',
            name='starttime',
        ),
        migrations.AlterField(
            model_name='date',
            name='dates',
            field=models.DateTimeField(null=True),
        ),
    ]
