# Generated by Django 4.2.2 on 2023-12-09 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_comment_story'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
    ]
