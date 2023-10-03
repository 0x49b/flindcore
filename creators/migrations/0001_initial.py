# Generated by Django 4.2.5 on 2023-10-03 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('yt_url', models.URLField()),
                ('yt_scrape', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CreatorMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber_count', models.IntegerField()),
            ],
        ),
    ]