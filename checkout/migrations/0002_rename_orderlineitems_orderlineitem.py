# Generated by Django 3.2.9 on 2021-11-25 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderLineItems',
            new_name='OrderLineItem',
        ),
    ]
