# Generated by Django 3.1 on 2021-04-06 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='category',
            new_name='genre',
        ),
    ]