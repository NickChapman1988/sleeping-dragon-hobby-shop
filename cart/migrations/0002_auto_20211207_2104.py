# Generated by Django 3.2.9 on 2021-12-07 21:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='valid_from',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discount',
            name='valid_to',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
