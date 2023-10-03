# Generated by Django 4.2.5 on 2023-10-03 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proxies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(unique=True)),
                ('port', models.IntegerField()),
                ('code', models.CharField(max_length=3)),
                ('country', models.CharField(max_length=256)),
                ('anonimity', models.CharField(max_length=256)),
                ('google', models.BooleanField(default=False)),
                ('https', models.BooleanField(default=False)),
                ('last_checked', models.CharField(max_length=512)),
            ],
        ),
    ]