# Generated by Django 3.2.6 on 2021-10-06 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20211006_0428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='activityimage',
        ),
        migrations.AlterField(
            model_name='activity',
            name='activitydetails',
            field=models.TextField(max_length=2000),
        ),
    ]
