# Generated by Django 3.2.23 on 2024-01-09 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20240109_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat1',
            name='friendly_name',
        ),
        migrations.RemoveField(
            model_name='cat2',
            name='friendly_name',
        ),
        migrations.RemoveField(
            model_name='cat3',
            name='friendly_name',
        ),
        migrations.RemoveField(
            model_name='cat4',
            name='friendly_name',
        ),
        migrations.AlterField(
            model_name='cat1',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cat2',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cat3',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cat4',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
