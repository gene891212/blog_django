# Generated by Django 3.1.3 on 2020-11-26 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20201125_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='datetime',
        ),
    ]