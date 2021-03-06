# Generated by Django 2.0 on 2020-06-01 12:27
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FanartType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'fanart_type',
                'managed': settings.TESTING,
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('release_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'media',
                'managed': settings.TESTING,
            },
        ),
        migrations.CreateModel(
            name='Platforms',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'platforms',
                'managed': settings.TESTING,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('publish_time', models.DateTimeField()),
                ('text_content', models.CharField(blank=True, max_length=300, null=True)),
                ('media_url', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'post',
                'managed': settings.TESTING,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pseudo', models.CharField(max_length=100)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=4)),
                ('date_of_birth', models.DateField()),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=4)),
                ('gender', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'app_user',
                'managed': settings.TESTING,
            },
        ),
        migrations.CreateModel(
            name='UserLibrairy',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'user_librairy',
                'managed': settings.TESTING,
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='backend.Media')),
                ('duration', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'film',
                'managed': settings.TESTING,
            },
        ),
        migrations.CreateModel(
            name='Tvshow',
            fields=[
                ('id', models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='backend.Media')),
                ('season_number', models.IntegerField()),
            ],
            options={
                'db_table': 'tvshow',
                'managed': settings.TESTING,
            },
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='backend.Media')),
            ],
            options={
                'db_table': 'video_game',
                'managed': settings.TESTING,
            },
        ),
    ]
