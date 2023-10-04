# Generated by Django 4.2.5 on 2023-10-04 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0002_alter_creatorusername_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='yt_scrape',
            field=models.BooleanField(default=True, verbose_name='Scrape'),
        ),
        migrations.AlterField(
            model_name='creator',
            name='yt_url',
            field=models.URLField(verbose_name='Youtube URL'),
        ),
    ]