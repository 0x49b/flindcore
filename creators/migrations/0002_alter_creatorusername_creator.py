# Generated by Django 4.2.5 on 2023-10-04 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatorusername',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creators.creator'),
        ),
    ]
