# Generated by Django 2.0.5 on 2018-05-18 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picksong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.TextField(default='song')),
                ('owner', models.TextField(default='owner')),
                ('key_of_song', models.TextField(default='Bb')),
                ('submission_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'songtest',
            },
        ),
    ]
