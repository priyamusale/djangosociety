# Generated by Django 3.1.7 on 2021-04-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('creator_name', models.CharField(max_length=100)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('location', models.TextField()),
                ('event_title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('members', models.TextField()),
                ('description', models.TextField()),
                ('category', models.TextField()),
                ('website_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField()),
                ('birth_date', models.DateField()),
                ('fav_movies', models.TextField()),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('username', models.CharField(max_length=100)),
                ('photo_url', models.URLField()),
            ],
        ),
    ]