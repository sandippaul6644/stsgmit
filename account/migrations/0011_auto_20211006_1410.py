# Generated by Django 3.2.6 on 2021-10-06 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20211006_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='questioncategory',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]