# Generated by Django 3.1.7 on 2021-04-10 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]