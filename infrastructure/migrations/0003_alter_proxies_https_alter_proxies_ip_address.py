# Generated by Django 4.2.5 on 2023-10-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0002_alter_proxies_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxies',
            name='https',
            field=models.BooleanField(default=False, verbose_name='HTTPS'),
        ),
        migrations.AlterField(
            model_name='proxies',
            name='ip_address',
            field=models.GenericIPAddressField(unique=True, verbose_name='IP Address'),
        ),
    ]
