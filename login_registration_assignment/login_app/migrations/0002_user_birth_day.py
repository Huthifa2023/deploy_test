# Generated by Django 4.2.7 on 2023-11-29 17:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_day',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]