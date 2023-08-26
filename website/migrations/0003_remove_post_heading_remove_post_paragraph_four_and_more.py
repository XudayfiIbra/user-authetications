# Generated by Django 4.1.4 on 2023-08-25 03:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_post_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='post',
            name='paragraph_four',
        ),
        migrations.RemoveField(
            model_name='post',
            name='paragraph_one',
        ),
        migrations.RemoveField(
            model_name='post',
            name='paragraph_three',
        ),
        migrations.RemoveField(
            model_name='post',
            name='paragraph_two',
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]