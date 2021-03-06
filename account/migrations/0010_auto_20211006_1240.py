# Generated by Django 3.2.6 on 2021-10-06 07:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_activity_activityowner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
        migrations.RemoveField(
            model_name='question',
            name='questionfile',
        ),
        migrations.RemoveField(
            model_name='question',
            name='questionimage',
        ),
        migrations.RemoveField(
            model_name='questioncategory',
            name='details',
        ),
        migrations.AlterField(
            model_name='answer',
            name='questionid',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='solver',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='headlines',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='owner',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='owner',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='questioncategory',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questioncategory',
            name='name',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='questioncategory',
            name='owner',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questioncategory',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
