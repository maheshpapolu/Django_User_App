# Generated by Django 4.0.6 on 2022-08-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
