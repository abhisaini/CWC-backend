# Generated by Django 2.0.6 on 2018-07-19 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cwc', '0006_auto_20180719_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
    ]
