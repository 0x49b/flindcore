# Generated by Django 4.2.5 on 2023-10-03 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('channel_id', models.CharField(max_length=25)),
                ('etag', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=1024)),
                ('localized_title', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('published_at', models.DateTimeField()),
                ('thumbnail', models.URLField()),
                ('related_playlists', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='TopicCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ChannelStatistics',
            fields=[
                ('created', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('channel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='yt_channels.channel')),
                ('view_count', models.BigIntegerField()),
                ('subscriber_count', models.BigIntegerField()),
                ('hidden_subscriber_count', models.BooleanField(default=False)),
                ('video_count', models.BigIntegerField()),
            ],
        ),
    ]
