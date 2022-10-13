# Generated by Django 4.1 on 2022-10-12 17:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesman',
            name='task',
        ),
        migrations.RemoveField(
            model_name='salesman',
            name='user',
        ),
        migrations.AddField(
            model_name='salesman',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]