# Generated by Django 4.2 on 2023-04-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='butterfly',
            name='species',
        ),
        migrations.RemoveField(
            model_name='butterfly',
            name='wingspan',
        ),
        migrations.AddField(
            model_name='butterfly',
            name='color',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='butterfly',
            name='stage',
            field=models.CharField(default='unknown', max_length=50),
        ),
    ]
